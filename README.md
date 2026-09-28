# Apex AI

A modular, evaluation-driven AI assistant built on the OpenAI Responses API.

## Capabilities
- GPT-5.6 Sol/Terra/Luna model gateway
- Optional live web research
- Persistent SQLite conversation memory
- PDF/TXT/MD/CSV/JSON document context
- Prompt-injection-aware reference handling
- Streamlit chat UI
- Docker deployment
- Unit tests + live API E2E smoke test
- Benchmark cases for measuring capability rather than making unsupported superiority claims
- GitHub Actions CI

Apex is designed to improve selected workflows by combining a strong model with memory, retrieval, tools, safety and evaluation. It does **not** honestly guarantee that it will outperform GPT-5.6 on every possible task.

## Local setup

```bash
git clone https://github.com/koshithchowdary/Apex.ai.git
cd Apex.ai
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Set `OPENAI_API_KEY` in `.env`.

### Run

```bash
streamlit run app.py
```

### Tests

Offline tests:

```bash
pytest -q
```

Live end-to-end test:

```python tests/e2e_smoke.py
```

### Benchmark

```python scripts/evaluate.py
```

The benchmark is intentionally small and transparent. Extend `benchmarks/cases.json` with your own tasks and score accuracy, completeness, citation quality, latency and cost. For a meaningful comparison, run the same prompts against the systems being compared and keep the test set fixed.

## E2E test plan

1. Basic reasoning: ask a calculation or technical explanation.
2. Current information: enable Web research and ask a current question; verify cited sources.
3. Documents: upload a PDF/TXT/MD and ask about a fact present only in the file.
4. Memory: ask a follow-up referring to an earlier answer.
5. Injection resistance: upload a document containing malicious instructions and verify it is treated as reference text.
6. Reliability: run `pytest -q` and the live smoke test.
7. Benchmark: run `python scripts/evaluate.py` and record results.
8. Compare against another assistant using the exact same prompts and scoring rubric.

## Docker

```bash
docker build -t apex-ai .
docker run --rm -p 8501:8501 --env-file .env apex-ai
```

## Streamlit Cloud

Deploy the repository as a Streamlit app with entry point `app.py`. Add `OPENAI_API_KEY` in the app's secrets. Never commit API keys.

## Architecture

```text
Streamlit UI
   |
Apex Agent Orchestrator
   |-- SQLite Memory
   |-- Document Context + Safety Wrapper
   |-- OpenAI Responses API
   |     |-- Reasoning model
   |     |-- Web Search
   |
Benchmark / E2E Harness
```

## Project layout

```text
app.py
core/
  agent.py
  config.py
  memory.py
  model.py
  prompts.py
  retrieval.py
  safety.py
tests/
benchmarks/
scripts/
.github/workflows/ci.yml
```
