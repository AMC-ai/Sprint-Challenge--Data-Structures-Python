class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if new < node.value
        if value < self.value:
            #       if left doesn't exist
            if self.left is None:
                #                 create left
                self.left = BinarySearchTree(value)
        #    leftnode.insert value
            else:
                self.left.insert(value)
        else:  # Value is greater than or equal to
            # if >=
            #  if right doesn't exist
            if self.right is None:
                #  create right
                self.right = BinarySearchTree(value)
        #  else
        #    rightnode.insertvalue
            else:
                self.right.insert(value)

        # Return True if the tree contains the value
        # False if it does not
    def contains(self, target):
        # if node.value == findvalue
        #     return true
        if self.value == target:
            return True
        if target < self.value:
           # else
            #     if find <  node.value
            #            find on  left node
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
            #     else
            #     find on right node
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

        # Return the maximum value found in the tree
    def get_max(self):
        # the right child is none is the base case
        # if there's a right:
        if self.right:
            #    get max on  right
            return self.right.get_max
        # else
        else:
            #    return node.value
            return self.value

        # Call the function `cb` on the value of each node
        # You may use a recursive or iterative approach
        # pre order traversal
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
