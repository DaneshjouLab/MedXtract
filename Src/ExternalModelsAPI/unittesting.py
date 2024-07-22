import unittest
from messages import Message

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


if __name__ == '__main__':
    unittest.main()