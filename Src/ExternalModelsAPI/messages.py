# you have many data objects, but only 

class Message:
    """
    builds Messages for the api's
    
    """

    # Currently a message only contains the content and sender information could add content type to future proof
    def __init__(self, **kwargs):
        if 'content' in kwargs and 'sender' in kwargs:
            self.content = kwargs['content']
            self.sender = kwargs['sender']
        else:
            raise AttributeError("Invalid input: must provide 'content' and 'sender' attributes")

    def getContent(self):
        return self.content
    
    def getSender(self):
        return self.sender

    


