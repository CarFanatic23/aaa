# Context

class Context:
    def __init__(self, display_name, parent = None, parent_en_pos = None):
        self.display_name = display_name
        self.parent = parent
        self.parent_en_pos = parent_en_pos
        self.sym_table = None