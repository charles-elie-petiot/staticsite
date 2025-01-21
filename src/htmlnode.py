class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ''
        string = ''
        for item in self.props.items():
            string += f' {item[0]}="{item[1]}"'
        return string
    
    def __repr__(self):
        if self.props == None:
           return f"HTMLNode({self.tag}, {self.value}, {self.children}, None)"
        else: 
             return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props.items()})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        elif self.tag == None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        if self.props == None:
           return f"LeafNode({self.tag}, {self.value}, {self.children}, None)"
        else: 
             return f"LeafNode({self.tag}, {self.value}, {self.children}, {self.props.items()})"
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError('No tag')
        elif self.children == None or len(self.children) == 0:
            raise ValueError('Missing children')
        else:
            string = ''
            for child in self.children:
                string += child.to_html()

            return f"<{self.tag}{self.props_to_html()}>{string}</{self.tag}>"
        
    def __repr__(self):
        if self.props == None:
           return f"ParentNode({self.tag}, {self.value}, {self.children}, None)"
        else: 
             return f"ParentNode({self.tag}, {self.value}, {self.children}, {self.props.items()})"
