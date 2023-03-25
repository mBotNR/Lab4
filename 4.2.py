class Stack:
    def __init__(self, stack, max):
        self.stack = [1, 2, 3]
        self.max = [3, 4, 1]

    def __pop__(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        if len(self.stack) == 0:
            self.max = None
        elif removed == self.max:
            self.max = self.stack[0]
            for value in self.stack:
                if value > self.max:
                    self.max = value
        return removed

    def __push__(self, item):
        self.stack.append(item)
        if len(self.stack) == 1 or item > self.max:
            self.max = item

    def __append__(self):
        pass

    def __copy__(self):
        pass

    def __extend__(self):
        pass

    def __next__(self):
        pass
