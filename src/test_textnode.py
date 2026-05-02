import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is not a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

        node = TextNode("This is a node", TextType.BOLD)
        node2 = TextNode("This is a node", TextType.BOLD)
        self.assertEqual(node, node2)

        node = TextNode("This is a text node", TextType.BOLD, "http://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node, node2)

def test_text(self):
    node = TextNode("This is a text node", TextType.TEXT)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.value, "This is a text node")

def test_bold(self):
    node = TextNode("**THIS IS BOLD**", TextType.BOLD)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "b")
    self.assertEqual(html_node.value, "**THIS IS BOLD**")

def test_italic(self):
    node = TextNode("_This is italic_", TextType.ITALIC)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "i")
    self.assertEqual(html_node.value, "_This is italic_")

def test_code(self):
    node = TextNode("<<<This is code>>>", TextType.CODE)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "code")
    self.assertEqual(html_node.value, "<<<This is code>>>")

def test_link(self):
    node = TextNode("Boot.dev!", TextType.LINK, "http://www.boot.dev")
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "a")
    self.assertEqual(html_node.value, "Boot.dev!")
    self.assertEqual(html_node.props["href"], "http://www.boot.dev")

def test_image(self):
    node = TextNode("Boots the Bear!", TextType.IMAGE, "http://www.boot.dev")
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "img")
    self.assertEqual(html_node.props["src"], "http://www.boot.dev")
    self.assertEqual(html_node.props["alt"], "Boots the Bear!")

def test_error(self):
    node = TextNode("OOPS!", TextType.OOPS)
    with self.assertRaises(Exception):
        text_node_to_html_node(node)


if __name__ == "__main__":
    unittest.main()