# you have many data objects, but only 

class Message:
    """
    builds Messages for the api's
    
    """

    # Currently a message only contains the content and sender information could add content type to future proof
    def __init__(self, **kwargs):
        allowed_attributes = {'content': None, 'sender': None}
        
        for key, value in kwargs.items():
            if key in allowed_attributes:
                setattr(self, key, value)
            else:
                raise AttributeError(f"Invalid attribute: {key}")
            
        for key in allowed_attributes:
            if not hasattr(self, key):
                setattr(self, key, allowed_attributes[key])

    def getContent(self):
        return self.content
    
    def getSender(self):
        return self.sender

    


