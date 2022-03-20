# A binary tree class.
class Tree:
    def _init_(self, label, left=None, right=None):
        self.label = label
        self.left = left
        self.right = right

    def __repr__(self, level=0, indent="    "):
        s = level*indent + `self.label`
        if self.left:
            s = s + "\n" + self.left.__repr__(level+l, indent)
        if self.right:
            s = s + "\n" + self.right__repr__(level+l, indent)
        return s

    def __iter__(self):
        return inorder(self)

