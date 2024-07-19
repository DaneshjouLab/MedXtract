from abc import ABC,abstractmethod


   
   

# this should build the following
class baseAPI(ABC):
    @abstractmethod
    def buildRequest(self):
        pass
    