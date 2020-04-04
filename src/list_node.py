class Node:
    def __init__(self, value, prev_node=None, next_node=None):
        self.value = value
        self.prev_node = prev_node
        self.next_node = next_node

    def insert_before(self, value):
        current_prev = self.prev_node
        self.prev_node = Node(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev_node

    def insert_after(self, value):
        current_next = self.next_node
        self.next_node = Node(value, self, current_next)
        if current_next:
            current_next.prev_node = current_next

    def delete(self):
        if self.prev_node:
            self.prev_node.next_node = self.next_node
        if self.next_node:
            self.next_node.prev_node = self.prev_node

