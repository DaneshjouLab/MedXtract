import os
from baseAPI import baseAPI
from Prompt_List import Prompt_List
from Message import Message
from openai import OpenAI
from Config.OpenAI_Config import OpenAIConfig
from dotenv import load_dotenv
import json
from dataclasses import asdict

load_dotenv()

class OpenAI_API(baseAPI):
    # Config/Dataclasses
    def __init__(self, **kwargs):
        if 'json_path' in kwargs:
            with open(kwargs['json_path'], 'r') as f:
                config_data = json.load(f)
            self.config = OpenAIConfig(**config_data)
        else:
            if 'model' not in kwargs:
                raise AttributeError(f"'Model' attribute required:")
            self.config = OpenAIConfig(**kwargs)

        self.client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

    def formatRequest(self, **kwargs):
        if 'prompt_list' in kwargs and isinstance(kwargs['prompt_list'], Prompt_List):
            prompt_list = kwargs['prompt_list'].getList()
            messages = []
            for message in prompt_list:
                messages.append({"role": message.getRole(), "content": message.getContent})
            self.config['messages'] = messages
        else:
            raise AttributeError(f"'prompt_list' attribute required:")
    
    def sendRequest(self):  
        response = self.client.chat.completions.create(**asdict(self.config))
        return response

    def unpackageResponse(self, **kwargs):
        if 'response' in kwargs:
            return kwargs['response'].choices[0].message.content
        else:
            raise AttributeError(f"'response' attribute required:")
        
    def getConfig(self):
        return asdict(self.config)
    