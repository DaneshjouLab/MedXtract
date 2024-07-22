# you have many data objects, but only 
# the following 
from abc import ABC

class Message(ABC):
    """
    builds Messages for the api's
    
    """
    def __init__(self):
    
        pass

    def buildMessage():
        pass
class TextContent:
    def __init__(self, text):
        self.type = "text"
        self.text = text

    def to_dict(self):
        return {"type": self.type, "text": self.text}

class Message:
    
    contentDictionary={}
    def __init__(self, role,prompt=None):
        self.role = role
        self.content = []
        
        if not (prompt is None):
            self.buildTextMessage(prompt)


    def add_text(self, text):
        self.content.append(TextContent(text))
    # def add_image(self, image_url=None, base64_str=None):
    #     self.content.append(ImageContent(image_url, base64_str))

    def to_dict(self):
        self.contentDictionary={"role": self.role, "content": [c.to_dict() for c in self.content]}
        return self.contentDictionary
    
    def buildTextMessage(self,prompt):
       self.add_text(prompt)
       self.to_dict()
       return


        
# take a list of messages and construct the following. 
class MessageConstructor():

    def __init__(self,**kwargs):
        #load message
        messages=[]
        pass
    def addUserMessage(self,prompt):
        return
    def addSystemPrompt(self, prompt):
        return
    def addAssistantPrompt(self,prompt):
        user="Assistant"
        return
