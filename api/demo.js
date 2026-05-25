export default async function handler(req, res) {
  const input = (req.body && req.body.input) || "";
  const hasKey = Boolean(process.env.MIMO_API_KEY);
  const mode = hasKey ? "mimo-ready" : "mock-demo";
  const project = "mimo-docs-translator";
  const task = "translate";
  const mock = {"language": "id", "markdown": "## Instalasi\n\nJalankan:\n```bash\nnpm install\n```"};
  return res.status(200).json({
    ok: true,
    project,
    task,
    mode,
    input_preview: input.slice(0, 500),
    result: mock,
    next_step: hasKey ? "Connect live MiMo request in this API route." : "Set MIMO_API_KEY in Vercel Environment Variables to enable real MiMo calls."
  });
}
