from openai import OpenAI
class ModelGateway:
    def __init__(self,settings):
        settings.validate(); self.s=settings; self.client=OpenAI(api_key=settings.api_key)
    def respond(self,instructions,input_items,use_web=True):
        kw={"model":self.s.model,"instructions":instructions,"input":input_items}
        if self.s.reasoning_effort: kw["reasoning"]={"effort":self.s.reasoning_effort}
        if use_web and self.s.enable_web: kw["tools"]=[{"type":"web_search"}]
        return self.client.responses.create(**kw)
