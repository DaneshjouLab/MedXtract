from messages import Message

class Prompt:
    """""
        The prompt class is a glorified list contrained to only carry messages
    """""
    def __init__(self):
        self.messageList = []
    
    # functionality allows either the input of a Message variable or the content and sender of a message
    def add(self, **kwargs):
        if 'message' in kwargs and isinstance(kwargs['message'], Message):
            self.messageList.append(kwargs['message'])
        elif 'content' in kwargs and 'sender' in kwargs:
            message = Message(content=kwargs['content'], sender=kwargs['sender'])
            self.messageList.append(message)
        else:
            raise AttributeError("Invalid input: must provide either a Message instance or 'content' and 'sender' attributes")

    def insert(self, index, **kwargs):
        if 'message' in kwargs and isinstance(kwargs['message'], Message):
            self.messageList.insert(index, kwargs['message'])
        elif 'content' in kwargs and 'sender' in kwargs:
            message = Message(content=kwargs['content'], sender=kwargs['sender'])
            self.messageList.insert(index, message)
        else:
            raise AttributeErrorError("Invalid input: must provide either a Message instance or 'content' and 'sender' attributes")

    def pop(self):
        self.messageList.pop()

    def peek(self):
        return self.messageList[len(self.messageList) - 1]

    def clear(self):
        self.messageList = []

    def getList(self):
        return self.messageList

        
    

