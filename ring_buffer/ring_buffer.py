from doubly_linked_list import DoublyLinkedList

# Implement this behavior in the RingBuffer class. RingBuffer has two methods, append and get. The append method adds elements to the buffer. The get method, which is provided, returns all of the elements in the buffer in a list in their given order. It should not return any None values in the list even if they are present in the ring buffer.

# You may not use a Python List in your implementation of the append method (except for the stretch goal)


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # checking if capacity is full
        if self.storage.length < self.capacity:
            # if not full add new item to tail
            self.storage.add_to_tail(item)
            # update current storage
            self.current = self.storage.head
        # if storage is full else/if to remove old data
        elif self.storage.length == self.capacity:
            # initialize removing old
            remove_head = self.storage.head
            # remove old item from head
            self.storage.remove_from_head()
            # add newest item to tail
            self.storage.add_to_tail(item)
            # check position
            if remove_head == self.current:
                # then move to tail
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
