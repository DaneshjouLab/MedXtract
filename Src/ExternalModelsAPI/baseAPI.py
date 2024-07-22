from abc import ABC,abstractmethod


   
   

# this should build the following
class baseAPI(ABC):
    @abstractmethod
    def __init__(self, **kwargs):
        pass

    # should take in an instance of the Prompt class
    def formatRequest(self):
        pass

    def sendRequest(self):
        pass

    def unpackageResponse(self):
        pass
    