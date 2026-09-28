import json
from pathlib import Path
from core.agent import ApexAgent
from core.config import Settings
if __name__=="__main__":
    a=ApexAgent(Settings())
    for c in json.loads(Path("benchmarks/cases.json").read_text()):
        ans,_=a.answer(c["prompt"],use_web=c["web"]); print("\n== "+c["id"]+" ==\n"+ans)
