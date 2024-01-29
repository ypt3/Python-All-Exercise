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

        print("Before add_child:")
        print("Child's parent:", child.parent)
        print("Parent's children:", parent.children)

        parent.add_child(child)

        print("After add_child:")
        print("Child's parent:", child.parent)
        print("Parrent's children:", parent.children)

        self.assertIn(child, parent.children)
        self.assertEqual(child.parent, parent)

    def test_remove_child(self):
        parent = Node("parent")
        child = Node("child")
        parent.add_child(child)
        parent.remove_child(child)
        self.assertNotIn(child, parent.children)
        self.assertIsNone(child.parent)

    def test_parent_setter(self):
        parent1 = Node("parent1")
        parent2 = Node("parent2")
        child = Node("child")

        child.parent = parent1
        self.assertIn(child, parent1.children)
        self.assertEqual(child.parent, parent1)

        child.parent = parent2
        self.assertNotIn(child, parent1.children)
        self.assertIn(child, parent2.children)
        self.assertEqual(child.parent, parent2)

    def test_depth_search(self):
        # New test for depth search 
        root = Node("A")
        b = Node("B")
        c = Node("C")
        d = Node("D")
        e = Node("E")
        f = Node("F")

        root.add_child(b)
        root.add_child(c)
        b.add_child(d)
        b.add_child(e)
        c.add_child(f)

        result_depth = root.depth_search("E")
        self.assertIsNotNone(result_depth)
        self.assertEqual(result_depth.value, "E")

        result_depth_none = root.depth_search("X")
        self.assertIsNone(result_depth_none)


    def test_breadth_search(self):
        # New test for breadth_search 
        root = Node("A")
        b = Node("B")
        c = Node("C")
        d = Node("D")
        e = Node("E")
        f = Node("F")

        root.add_child(b)
        root.add_child(c)
        b.add_child(d)
        b.add_child(e)
        c.add_child(f)

        result_depth = root.depth_search("E")
        self.assertIsNotNone(result_depth)
        self.assertEqual(result_depth.value, "E")

        result_depth_none = root.depth_search("X")
        self.assertIsNone(result_depth_none)


# Example usage: 
parent = Node("parent")
child = Node("child")

parent.add_child(child)

print("Child's parent:", child.parent)
print("Parent's children", [child.value for child in parent.children])

if __name__ == '__main__':
    unittest.main()