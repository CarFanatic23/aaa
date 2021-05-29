# Position

class Position:
    def __init__(self, idx, ln, col, fn, fc):
        self.idx = idx
        self.ln = ln
        self.col = col
        self.fn = fn
        self.fc = fc

    def advance(self, curr):
        '''Advance to next position.'''
        self.idx += 1
        self.col += 1 if curr != '\n' else -self.col
        # ^ add 1 if `curr` is not a new line char else add negative of `self.col` which resets `self.col` to 0
        self.ln += 0 if curr != '\n' else 1

        return self

    def copy(self):
        '''Makes a copy of itself.'''
        return Position(self.idx, self.ln, self.col, self.fn, self.fc)