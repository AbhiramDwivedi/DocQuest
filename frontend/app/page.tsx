"use client";
import { useState } from "react";
export default function Home() {
  const [q, setQ] = useState("");
  const [answer, setAnswer] = useState<string | null>(null);
  async function onAsk(e: React.FormEvent) {
    e.preventDefault();
    setAnswer(`(stub) You asked: ${q}`);
  }
  return (
    <main style={{ padding: 24 }}>
      <h1>DocQuest</h1>
      <p>Local-first enterprise document search (MCP).</p>
      <form onSubmit={onAsk} style={{ display: "flex", gap: 8 }}>
        <input value={q} onChange={(e) => setQ(e.target.value)} placeholder="Ask about your docs..." style={{ flex: 1, padding: 8 }} />
        <button type="submit">Ask</button>
      </form>
      {answer && (<section style={{ marginTop: 16 }}>
        <h3>Answer</h3><pre>{answer}</pre>
      </section>)}
    </main>
  );
}
