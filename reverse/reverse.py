class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we
        # traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our
            # target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self, node, prev):
        # You must use recursion for this solution
        current_node = self.head
        prev_node = None

        # iterate thru single linked list
        # set base
        while current_node is not None:
            # store next node value
            next_node = current_node.get_next()
            # change next of current node to prev_node ("shift over" the value)
            current_node.set_next(prev_node)
            # prev node = current_node (value has "shifted" to prev_node)
            prev_node = current_node
            # and current_node = next_node (values are reversed or "shifted")
            current_node = next_node
            # reverse list now provides reverse list node values 1-2-3-none -> 3-2-1-none
        self.head = prev_node
