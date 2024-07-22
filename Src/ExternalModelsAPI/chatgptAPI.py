from baseAPI import baseAPI
from prompt_list import Prompt
from messages import Message
from openai import OpenAI

class ChatGPT(baseAPI):
    def __init__(self, **kwargs):
        allowed_attributes = {'model': None, 'api_key': None}
        
        for key, value in kwargs.items():
            if key in allowed_attributes:
                setattr(self, key, value)
            else:
                raise AttributeError(f"Invalid attribute: {key}")
            
        for key in allowed_attributes:
            if not hasattr(self, key):
                setattr(self, key, allowed_attributes[key])
        self.client = OpenAI(api_key = self.api_key)

    def formatRequest(self, **kwargs):
        pass 

    def sendRequest(self, **kwargs):
        
        pass
    def unpackageResponse(self, **kwargs):
        pass