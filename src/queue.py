from dll import DLL


class Queue:
    def __init__(self):
        self.storage = DLL()

    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.add_to_head(value)

    def dequeue(self):
        if not self.storage.head:
            return
        return self.storage.remove_from_tail()
