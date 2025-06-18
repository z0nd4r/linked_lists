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

        next_val = self.__head.next
        self.__head = None
        self.__head = next_val

        print(f'removed_head: {removed_value}')

    def remove_last(self):
        if self.__is_empty():
            print(ValueError(f'{self.remove.__func__.__name__}: Cannot remove an element from an empty list'))

        removed_value = self.__tail

        val = self.__head
        next_val = self.__head.next
        
        while next_val != removed_value:
            val = next_val
            next_val = next_val.next

        self.__tail = None
        self.__tail = val

        print(f'removed_tail: {removed_value}')

    def remove(self, value):
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
                self.__head = next_val
            elif val == self.__tail:
                self.__tail = old_val
                old_val.next = None
            else:
                old_val.next = next_val
                val = None

            print(f'removed_value: {removed_value}')

        except:
            print(ValueError(f"{self.remove.__func__.__name__}: Cannot remove an element, he's not on the list"))

    def __is_empty(self):
        return self.__head is None

    def __initialize(self, new_node):
        self.__head = self.__tail = new_node


ll = LinkedList()
ll.add_last(13)
ll.add_first(1)
ll.add_first(2)
ll.add_last(34)
ll.remove(2)
# ll.remove(1)
ll.remove(13)
ll.remove(34)

print('')