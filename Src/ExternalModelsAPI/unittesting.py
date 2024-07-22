import unittest
from messages import Message

class TestMessage(unittest.TestCase):
    def test_initialization(self):
        content = "this is test content"
        sender = "user"
        message = Message(content = content, sender = sender)
        self.assertEqual(message.getContent(), content)
        self.assertEqual(message.getSender(), sender)

if __name__ == '__main__':
    unittest.main()