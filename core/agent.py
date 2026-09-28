from .config import Settings
from .memory import Memory
from .model import ModelGateway
from .prompts import SYSTEM_PROMPT
from .safety import wrap_untrusted
class ApexAgent:
    def __init__(self,settings=None,memory=None):
        self.settings=settings or Settings(); self.memory=memory or Memory(); self.gateway=ModelGateway(self.settings)
    def answer(self,user_text,document_context="",use_web=True):
        history=[{"role":r,"content":c} for r,c in self.memory.recent(self.settings.max_memory_messages)]
        current=user_text
        if document_context: current+="\n\n"+wrap_untrusted(document_context)
        response=self.gateway.respond(SYSTEM_PROMPT,history+[{"role":"user","content":current}],use_web)
        text=response.output_text
        self.memory.add("user",user_text); self.memory.add("assistant",text)
        return text,response
