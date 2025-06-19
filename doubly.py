class LinkedList:
    class __Node:
        def __init__(self, value):
            self.value = value
            self.prev = None
            self.next = None

        def __repr__(self):
            return f'value = {self.value}'

    def __init__(self):
        self.__head = None
        self.__tail = None