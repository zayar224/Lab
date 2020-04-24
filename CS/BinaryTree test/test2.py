class BinaryTree:
    
    def __repr__(self):
        return "Binary Tree, Key is" + self.key
    
    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child
    def get_left_child(self):
        return self.left_child
    def set_root_val(self, obj):
        self.key = obj
    def get_root_val(self):
        return self.key

    """def bfs(self, value):
        thislevel = [self]
        while thislevel:
            nextlevel = []
            level = []
            for n in thislevel:
                if (level.append(n.get_root_val() == value)):
                    return True
                if n.get_left_child() != None:
                    if nextlevel.append(n.get_left_child()).bfs(value):
                        return True
                if n.get_right_child() != None:
                    if nextlevel.append(n,get_right_child()).bfs(value):
                        return True
                return False"""
    def bfs(self):
        thislevel = [self]
        while thislevel:
            nextlevel = []
            level = []
            for n in thislevel:
                level.append(n.get_root_val())
                if n.get_left_child() != None:
                    nextlevel.append(n.get_left_child())
                if n.get_right_child() != None:
                    nextlevel.append(n.get_right_child())
            print(",".join(level))
            thislevel = nextlevel

root = BinaryTree("A")
root.insert_left("B")
root.insert_right("C")

b = root.get_left_child()
b.insert_left("D")
b.insert_right("E")

d = root.get_right_child()
d.insert_left("F")
d.insert_right("G")

root.bfs()
"""found = root.bfs("A")
if found:
    print("Found")
else:
    print("Not Found")"""
