import os, json, requests
from openai import OpenAI

def get_event():
    with open(os.environ["GITHUB_EVENT_PATH"], "r", encoding="utf-8") as f:
        return json.load(f)

def fetch_pr_files(token, files_url):
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"}
    out = []
    url = files_url
    while url:
        r = requests.get(url, headers=headers, timeout=30)
        r.raise_for_status()
        out.extend(r.json())
        url = None
        if "next" in r.links:
            url = r.links["next"]["url"]
    return out

def post_comment(token, comments_url, body):
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"}
    r = requests.post(comments_url, headers=headers, json={"body": body}, timeout=30)
    r.raise_for_status()

def main():
    event = get_event()
    pr = event["pull_request"]
    files = fetch_pr_files(os.environ["GITHUB_TOKEN"], pr["url"] + "/files")
    diffs = []
    char_budget = 15000
    used = 0
    for f in files:
      patch = f.get("patch", "")
      header = f"--- {f['filename']} ({f['status']})\n"
      block = header + patch + "\n"
      if used + len(block) > char_budget:
        break
      diffs.append(block); used += len(block)
    diff_text = "\n".join(diffs) or "(no diff or too large)"
    prompt = '''You are a senior staff engineer reviewing a pull request.
Assess code quality, correctness, security, dependency risks, and test coverage.
Point out specific issues with actionable suggestions; be concise, bullet where helpful.

Diff (truncated to {used} chars):
{diff_text}
'''.format(used=used, diff_text=diff_text)
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    resp = client.chat.completions.create(
      model=os.environ.get("DOCQUEST_REVIEW_MODEL", "gpt-5"),
      messages=[
        {"role":"system","content":"Be rigorous, practical, and kind. Prefer specific suggestions over generalities."},
        {"role":"user","content": prompt}
      ],
      temperature=0.2,
    )
    review = resp.choices[0].message.content
    body = f"## 🤖 LLM PR Review\n\n{review}\n\n> Model: {os.environ.get('DOCQUEST_REVIEW_MODEL','gpt-5')}"
    post_comment(os.environ["GITHUB_TOKEN"], pr["_links"]["comments"]["href"], body)

if __name__ == "__main__":
    main()
