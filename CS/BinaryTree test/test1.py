class BinaryTree:
    def __repr__(self):
        return "Binary Tree, Key is " + self.key

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

    def inorder(self, argu):
        if self != None:
            if self.get_left_child() != None:
                if self.get_left_child().inorder(argu):
                    return True
                if (self.get_root_val() == argu):
                    return True
                if self.get_right_child() != None:
                    if self.get_right_child().inorder(argu):
                        return True
                return False


root = BinaryTree("A")
root.insert_left("B")
root.insert_right("C")

b = root.get_left_child()
b.insert_left("D")
b.insert_right("E")

c = root.get_right_child()
c.insert_left("F")
c.insert_right("G")

argu = str(input("Enter Some One Alphabet : "))
root.inorder(argu)
if root.inorder(argu):
    print("Found")
else:
    print("Not Found")
"""for i in arr:
    if alpha == "A":
        print("True")
    else:
        print("False")"""
