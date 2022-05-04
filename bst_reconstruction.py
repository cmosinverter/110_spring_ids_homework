class Node:
 
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BST :
 
    def constructBST(self, pre, size):
   
        root = Node(pre[0])
        stack = [root]
        for i in range(1, N):
            # add left if this value is smaller than current node
            if stack[-1].data > pre[i]:
                stack[-1].left = Node(pre[i])
                stack.append(stack[-1].left)
            # find which node to add right from the stack
            else:
                while stack and stack[-1].data < pre[i]:
                    tmp = stack.pop()
                tmp.right = Node(pre[i])
                stack.append(tmp.right)
        
        return root

    def printInorder(self, node):
        if not node: return
        
        self.printInorder(node.left)
        print(node.data, end = " ")
        self.printInorder(node.right)
        
    def printPostorder(self, node):
        if not node: return
        
        self.printPostorder(node.left)
        self.printPostorder(node.right)
        print(node.data, end = " ")
        
if __name__ == "__main__":
    tree = BST()
    N = int(input())
    pre = list(map(int, input().split()))
    root = tree.constructBST(pre, N)
    tree.printInorder(root)
    print(end = '\n')
    tree.printPostorder(root)
