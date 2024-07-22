# you have many data objects, but only 
# test2
class Messages:
    """
    builds Messages for the api's
    
    """
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

    


