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

    def add_first(self, value):
        new_node = self.__Node(value)
        if self.__is_empty():
            self.__initialize(new_node)
        else:
            new_node.next = self.__head
            self.__head.prev = new_node
            self.__head = new_node

    def add_last(self, value):
        new_node = self.__Node(value)
        if self.__is_empty():
            self.__initialize(new_node)
        else:
            self.__tail.next = new_node
            new_node.prev = self.__tail
            self.__tail = new_node

    def remove_first(self):
        if self.__is_empty():
            print(f'{self.remove_first.__func__.__name__}Cannot remove an element from an empty list')
            return

        removed_value = self.__head

        self.__head.next.prev = None
        self.__head = self.__head.next

        print(f'removed_head: {removed_value}')

    def remove_last(self):
        if self.__is_empty():
            print(f'{self.remove_last.__func__.__name__}Cannot remove an element from an empty list')
            return

        removed_value = self.__tail

        self.__tail = self.__tail.prev
        self.__tail.next = None

        print(f'removed_tail: {removed_value}')

    def remove(self, value):
        if self.__is_empty():
            print(f'{self.remove_last.__func__.__name__}: Cannot remove an element from an empty list')
            return

        removed_value = self.__Node(value)

        val = self.__head
        next_val = self.__head.next
        old_val = val

        try:
            while removed_value.value != val.value:
                old_val = val
                val = next_val
                next_val = val.next

            if val == self.__head and val == self.__tail:
                self.__head = None
                self.__tail = None
            elif val == self.__head:
                self.__head.next.prev = None
                self.__head = next_val
            elif val == self.__tail:
                self.__tail = old_val
                old_val.next = None
            else:
                old_val.next = next_val
                next_val.prev = old_val
                val = None

            print(f'removed_value: {removed_value}')

        except:
            print(f"{self.remove.__func__.__name__}: Cannot remove an element, he's not on the list")

    def print(self):
        pass

    def __is_empty(self):
        return self.__head is None

    def __initialize(self, new_node):
        self.__head = self.__tail = new_node


ll = LinkedList()
ll.add_first(1)
ll.add_first(2)
ll.add_first(5)
ll.add_last(4)
ll.remove(2)

print('')