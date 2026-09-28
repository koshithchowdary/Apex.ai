import os
from core.agent import ApexAgent
from core.config import Settings
if __name__=="__main__":
    if not os.getenv("OPENAI_API_KEY"): raise SystemExit("Set OPENAI_API_KEY first.")
    a=ApexAgent(Settings()); text,_=a.answer("Explain HTTP 417 in 5 bullets and distinguish client/protocol behavior from server causes.",use_web=False)
    assert text.strip(); print("E2E PASS\n"); print(text)
