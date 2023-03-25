class Stack:
    def __init__(self):
        self.stack =[]

    def __push__(self, item):
        self.stack.append(item)

    def __pop__(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        return removed

    def __append__(self):
        pass

    def __copy__(self):
        pass

    def __extend__(self):
        pass

    def __next__(self):
