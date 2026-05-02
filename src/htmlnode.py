class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag # representing HTML tag
        self.value = value # string representing value of HTML tag
        self.children = children # list of HTMLNode objects representing children of node
        self.props = props # dictionary of k-v pairs representing attributes of HTML tag

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        prop_string = ""
        if not self.props:
            return ""
        for i in self.props:
            prop_string += f' {i}="{self.props[i]}"'
        return prop_string
        
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return f"{self.value}"
        else:
            prop_string = self.props_to_html()
            return f"<{self.tag}{prop_string}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("This node needs a tag!")
        if not self.children:
            raise ValueError("This node needs children!")
        else:
            child_string = ""
            prop_string = self.props_to_html()
            for child in self.children:
                child_string += child.to_html()
            return f"<{self.tag}{prop_string}>{child_string}</{self.tag}>"
