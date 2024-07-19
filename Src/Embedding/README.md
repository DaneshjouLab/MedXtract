#Embeddings
This folder should efectively contain information and apckaging of embedding methods. 
Abstract from the storage databases

---a couple of toools to build. 
[ ]  create abstract embeddings class, 
        since you can have inifinite number of tokens, and inifnite number of models, it should really be as simple as an n dimensionaly array, that can be loaded distributively.... the idea here being that the array of the embeddings can be partitioned. ... either way we assume a data type of that class to handle it, 
        - should create some way to ensure distributed handling of this embedding. 
[ ]  create abstract data base--- there are many different tools out there, but equivalently you have an embedding and you want different types of search for it, this needs to be able to fulfill that core functionality without adding layers on top. 
 

[ ] of course the 

---