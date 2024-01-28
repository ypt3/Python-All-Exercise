import unittest
from tree import Node

class TestNodeMethods(unittest.TestCase):

    def test_init(self):
        node = Node("value")
        self.assertEqual(node.value, "value")
        self.assertIsNone(node.parent)
        self.assertEqual(node.children, [])

    def test_add_child(self):
        parent = Node("parent")
        child = Node("child")
        parent.add_child(child)
        self.assertIn(child, parent.children)
        self.assertEqual(child.parent, parent)

    