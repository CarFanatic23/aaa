# Nodes

class NumberNode:
    def __init__(self, tok):
        '''Number node.'''
        self.tok = tok

    def __repr__(self):
        return str(self.tok)

class BinOpNode:
    def __init__(self, left_node, op_tok, right_node):
        '''Binary operation node.'''
        self.left_node = left_node
        self.right_node = right_node
        self.op_tok = op_tok

    def __repr__(self):
        return f'({self.left_node}, {self.op_tok}, {self.right_node})'