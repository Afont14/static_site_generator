import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_single(self):
        node = HTMLNode(props={"href": "https://www.google.com", })
        result = node.props_to_html()
        self.assertEqual(result, ' href="https://www.google.com"')

    def test_empty(self):
        node = HTMLNode(props={})
        result = node.props_to_html()
        self.assertEqual(result, "")

    def test_multiple(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "http://www.boot.dev", })
        result = node.props_to_html()
        self.assertEqual(result, ' href="https://www.google.com" target="http://www.boot.dev"')



class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_no_tag(self):
        node = LeafNode(None, "There is no tag!")
        self.assertEqual(node.to_html(), "There is no tag!")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Boot.dev", {"href": "http://www.boot.dev"})
        self.assertEqual(node.to_html(), '<a href="http://www.boot.dev">Boot.dev</a>')

    def test_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()