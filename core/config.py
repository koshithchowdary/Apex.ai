import os
from dataclasses import dataclass
from dotenv import load_dotenv
load_dotenv()
@dataclass(frozen=True)
class Settings:
    api_key:str=os.getenv("OPENAI_API_KEY","")
    model:str=os.getenv("APEX_MODEL","gpt-5.6-sol")
    reasoning_effort:str=os.getenv("APEX_REASONING_EFFORT","high")
    enable_web:bool=os.getenv("APEX_ENABLE_WEB","true").lower() in {"1","true","yes"}
    max_memory_messages:int=int(os.getenv("APEX_MAX_MEMORY_MESSAGES","12"))
    def validate(self):
        if not self.api_key: raise ValueError("OPENAI_API_KEY is not configured.")
