# Nodes

class NumberNode:
    def __init__(self, tok):
        '''Number node.'''
        self.tok = tok

    def __repr__(self):
        return str(self.tok)

class BinOpNode:
    def __init__(self, left, op_tok, right):
        '''Binary operation node.'''
        self.left = left
        self.right = right
        self.op_tok = op_tok

    def __repr__(self):
        return f'({self.left}, {self.op_tok}, {self.right})'

class UnaryOpNode:
    def __init__(self, op_tok, node):
        '''Unary operation node.'''
        self.op_tok = op_tok
        self.node = node

    def __repr__(self):
        return f'({self.op_tok}, {self.node})'