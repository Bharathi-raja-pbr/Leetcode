    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def inorderTraversal(root):

            result=[]
            def inorder(root):
                if root is None:
                    result.append(0)
                    return 
                inorder(root.left)
                result.append(root.val)
                inorder(root.right)
            inorder(root)
            print(result)
            return result
        
        a=inorderTraversal(p)
        b=inorderTraversal(q)

        if a==b:
            return True
        else:
            return False
