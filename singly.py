class LinkedList:
    class __Node:
        def __init__(self, value):
            self.value = value
            self.next = None

        def __repr__(self):
            return f'value = {self.value}'

    def __init__(self):
        self.__head = None
        self.__tail = None

    def add_first(self, value):
        new_node = self.__Node(value)
        if self.__is_empty():
            self.__initialize(new_node)
        else:
            new_node.next = self.__head
            self.__head = new_node

    def add_last(self, value):
        new_node = self.__Node(value)
        if self.__is_empty():
            self.__initialize(new_node)
        else:
            self.__tail.next = new_node
            self.__tail = new_node

    def remove_first(self):
        if self.__is_empty():
            return ValueError('Cannot remove an element from an empty list')

        removed_value = self.__head

        next = self.__head.next
        self.__head = None
        self.__head = next

        print(f'removed: {removed_value}')

    def __is_empty(self):
        return self.__head is None

    def __initialize(self, new_node):
        self.__head = self.__tail = new_node


ll = LinkedList()
ll.add_last(13)
ll.add_first(1)
ll.add_first(2)
ll.add_last(34)
ll.remove_first()
print('')