from core.config import Settings
def test_defaults(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY","test")
    s=Settings(); assert s.model=="gpt-5.6-sol"
