# Nodes

class NumberNode:
    def __init__(self, tok):
        '''Number node.'''
        self.tok = tok
        self.pos_start = tok.pos_start
        self.pos_end = tok.pos_end

    def __repr__(self):
        return repr(self.tok)

class BinOpNode:
    def __init__(self, left, op_tok, right):
        '''Binary operation node.'''
        self.left = left
        self.right = right
        self.op_tok = op_tok
        self.pos_start = left.pos_start
        self.pos_end = right.pos_end

    def __repr__(self):
        return f'({self.left}, {self.op_tok}, {self.right})'

class UnaryOpNode:
    def __init__(self, op_tok, node):
        '''Unary operation node.'''
        self.op_tok = op_tok
        self.node = node
        self.pos_start = op_tok.pos_start
        self.pos_end = node.pos_end

    def __repr__(self):
        return f'({self.op_tok}, {self.node})'

class VarAssignNode:
    def __init__(self, tok, value_node):
        '''Variable assignment node.'''
        self.tok = tok
        self.value_node = value_node
        self.pos_start = tok.pos_start
        self.pos_end = value_node.pos_end

class VarAccessNode:
    def __init__(self, tok):
        '''Variable access node.'''
        self.tok = tok
        self.pos_start = tok.pos_start
        self.pos_end = tok.pos_end