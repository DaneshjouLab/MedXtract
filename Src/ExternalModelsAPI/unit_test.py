import unittest
from Message import Message
from Prompt_List import Prompt_List
#testing
class TestMessage(unittest.TestCase):
    def test_proper_initialization(self):
        content = "this is test content"
        role = "user"
        message = Message(content = content, role = role)
        self.assertEqual(message.getContent(), content)
        self.assertEqual(message.getRole(), role)

    def test_improper_initialization(self):
        content = "this is test content"
        role = "user"
        with self.assertRaises(AttributeError):
            message = Message(information = content, type = role)
     
    def test_empty_initialization(self):
        message = Message()
        self.assertEqual(message.getContent(), None)
        self.assertEqual(message.getRole(), None)

class TestPrompt(unittest.TestCase):
    def test_proper_initialization(self):
        prompt = Prompt_List()
        self.assertEqual(len(prompt.getList()), 0)

    def test_add(self):
        prompt = Prompt_List()
        content = "this is test add 1"
        role = "user"
        message = Message(content = content, role = role)
        prompt.add(message = message)
        self.assertEqual(len(prompt.getList()), 1)
        self.assertEqual(prompt.peek().getContent(), content)
        self.assertEqual(prompt.peek().getRole(), role)
        content = "this is test add 2"
        role = "assistant"
        prompt.add(content = content, role = role)
        self.assertEqual(len(prompt.getList()), 2)
        self.assertEqual(prompt.peek().getContent(), content)
        self.assertEqual(prompt.peek().getRole(), role)
        prompt.add()
        self.assertEqual(len(prompt.getList()), 3)
        self.assertEqual(prompt.peek().getContent(), None)
        self.assertEqual(prompt.peek().getRole(), None)
    
    def test_insert(self):
        prompt = Prompt_List()
        prompt.add(content = "this is test add 1", role = "user")
        prompt.add(content = "this is test add 2", role = "assistant")
        content = "this is test add 3"
        role = "user"
        index = 0
        prompt.insert(content = content, role = role, index = index)
        self.assertEqual(len(prompt.getList()), 3)
        self.assertEqual(prompt.getList()[index].getContent(), content)
        self.assertEqual(prompt.getList()[index].getRole(), role)
        content = "this is test add 4"
        role = "assistant"
        index = 2
        message = Message(content = content, role = role)
        prompt.insert(index = index, message = message)
        self.assertEqual(len(prompt.getList()), 4)
        self.assertEqual(prompt.getList()[index].getContent(), content)
        self.assertEqual(prompt.getList()[index].getRole(), role)
        index = 0
        prompt.insert(index = index)
        self.assertEqual(len(prompt.getList()), 5)
        self.assertEqual(prompt.getList()[index].getContent(), None)
        self.assertEqual(prompt.getList()[index].getRole(), None)
        content = "this is test add 6"
        role = "user"
        index = 4
        message = Message(content = content, role = role)
        with self.assertRaises(AttributeError):
            prompt.insert(message = message)
        
    def test_clear(self):
        prompt = Prompt_List()
        prompt.add(content = "this is test add 1", role = "user")
        prompt.add(content = "this is test add 2", role = "assistant")
        prompt.clear()
        self.assertEqual(len(prompt.getList()), 0)



if __name__ == '__main__':
    unittest.main()