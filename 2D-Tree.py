import random

class TreeNode:
    def __init__(self, key,disc = None):
        self.key = key
        self.dim = len(self.key)
        self.left = None
        self.right = None
        self.p = None
        self.disc = disc

    def getDisc(self):
        return self.key[self.disc]

    def __repr__(self):
        return "< %s %s >" % (self.key,self.p)

    def __str__(self):
        return "< %s %s >" % (self.key,self.p)

class BinaryTree:
    def __init__(self,keyDim):
        self.root = None
        self.keyDim = keyDim

    def length(self):
        return self.size

    def getRoot(self):
        return self.root

    def inorder(self, node):
        if node == None:
            return None
        else:
            self.inorder(node.left)
            print node.key,
            self.inorder(node.right)

    def search(self, k,f):
        node = self.root
        f.write(str(node.key))
        while node != None:
            if node.key == k:
                return node
            if node.key > k:
                node = node.left
            else:
                node = node.right
            f.write(str(node.key))
        return None

    def minimum(self, node):
        x = None
        while node.left != None:
            x = node.left
            node = node.left
        return x

    def maximum(self, node):
        x = None
        while node.right != None:
            x = node.right
            node = node.right
        return x

    def successor(self, node):
        parent = None
        if node.right != None:
            return self.minimum(node.right)
        parent = node.p
        while parent != None and node == parent.right:
            node = parent
            parent = parent.p
        return parent

    def predecessor(self, node):
        parent = None
        if node.left != None:
            return self.maximum(node.left)
        parent = node.p
        while parent != None and node == parent.left:
            node = parent
            parent = parent.p
        return parent

    def insert(self, k):
        if len(k)>1:
            if self.root == None:
                self.root = TreeNode(k,0)
                return True
            else:
                newNode = TreeNode(k,0)
                curRoot = self.root

                self.recursiveIns(curRoot,newNode)
        else:
            return False

    def recursiveIns(self,root,newNode):
        if newNode.getDisc() > root.getDisc():
            if root.right == None:
                root.right = newNode
                newNode.disc = (root.disc + 1) % self.keyDim
            else:
                self.recursiveIns(root.right,newNode)
        else:
            if root.left == None:
                root.left = newNode
                newNode.disc = (root.disc + 1) % self.keyDim
            else:
                self.recursiveIns(root.left,newNode)


    def delete(self, node):
        if node.left == None:
            self.transplant(node, node.right)
        elif node.right == None:
            self.transplant(node, node.left)
        else:
            succ = self.minimum(node.right)
            if succ.p != node:
                self.transplant(succ, succ.right)
                succ.right = node.right
                succ.right.p = succ
            self.transplant(node, succ)
            succ.left = node.left
            succ.left.p = succ

    def transplant(self, node, newnode):
        if node.p == None:
            self.root = newnode
        elif node == node.p.left:
            node.p.left = newnode
        else:
            node.p.right = newnode
        if newnode != None:
            newnode.p = node.p

if __name__ == "__main__":

    f = open('output.txt', 'w')
    B = BinaryTree(2);

    for i in range(10):
        for j in range(10):
            r1 = random.randint(1,100)
            r2 = random.randint(1,100)
            B.insert([r1,r2])

    B.insert([11,11])
    B.insert([22,22])
    B.insert([33,33])
    B.insert([44,44])
    B.insert([55,55])
    B.insert([66,66])
    B.insert([77,77])
    B.insert([88,88])
    B.insert([99,99])
    B.insert([100,100])

    B.search([100,100],f)
    f.close()
