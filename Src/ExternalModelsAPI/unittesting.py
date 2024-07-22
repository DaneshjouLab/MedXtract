import unittest
from messages import Message
from promptconstructor import Prompt

class TestMessage(unittest.TestCase):
    def test_proper_initialization(self):
        content = "this is test content"
        sender = "user"
        message = Message(content = content, sender = sender)
        self.assertEqual(message.getContent(), content)
        self.assertEqual(message.getSender(), sender)

    def test_improper_initialization(self):
        content = "this is test content"
        sender = "user"
        with self.assertRaises(AttributeError):
            message = Message(information = content, type = sender)
     
    def test_empty_initialization(self):
        message = Message()
        self.assertEqual(message.getContent(), None)
        self.assertEqual(message.getSender(), None)

class TestPrompt(unittest.TestCase):
    def test_proper_initialization(self):
        prompt = Prompt()
        self.assertEqual(len(prompt.getList()), 0)

    def test_add(self):
        prompt = Prompt()
        content = "this is test add 1"
        sender = "user"
        message = Message(content = content, sender = sender)
        prompt.add(message = message)
        self.assertEqual(len(prompt.getList()), 1)
        self.assertEqual(prompt.peek().getContent(), content)
        self.assertEqual(prompt.peek().getSender(), sender)
        content = "this is test add 2"
        sender = "assistant"
        prompt.add(content = content, sender = sender)
        self.assertEqual(len(prompt.getList()), 2)
        self.assertEqual(prompt.peek().getContent(), content)
        self.assertEqual(prompt.peek().getSender(), sender)
        prompt.add()
        self.assertEqual(len(prompt.getList()), 3)
        self.assertEqual(prompt.peek().getContent(), None)
        self.assertEqual(prompt.peek().getSender(), None)
    
    def test_insert(self):
        prompt = Prompt()
        prompt.add(content = "this is test add 1", sender = "user")
        prompt.add(content = "this is test add 2", sender = "assistant")
        content = "this is test add 3"
        sender = "user"
        index = 0
        prompt.insert(content = content, sender = sender, index = index)
        self.assertEqual(len(prompt.getList()), 3)
        self.assertEqual(prompt.getList()[index].getContent(), content)
        self.assertEqual(prompt.getList()[index].getSender(), sender)
        content = "this is test add 4"
        sender = "assistant"
        index = 2
        message = Message(content = content, sender = sender)
        prompt.insert(index = index, message = message)
        self.assertEqual(len(prompt.getList()), 4)
        self.assertEqual(prompt.getList()[index].getContent(), content)
        self.assertEqual(prompt.getList()[index].getSender(), sender)
        index = 0
        prompt.insert(index = index)
        self.assertEqual(len(prompt.getList()), 5)
        self.assertEqual(prompt.getList()[index].getContent(), None)
        self.assertEqual(prompt.getList()[index].getSender(), None)
        content = "this is test add 6"
        sender = "user"
        index = 4
        message = Message(content = content, sender = sender)
        with self.assertRaises(AttributeError):
            prompt.insert(message = message)
        



if __name__ == '__main__':
    unittest.main()