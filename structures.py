import pdb


class NodeItem:
    def __init__(self, ip: str, freq: int = 1):
        self.data: dict = {
            'freq': freq,
            'ip': ip,
        }
        self.prev: NodeItem = None
        self.next: NodeItem = None

    @property
    def value(self):
        freq = self.data['freq']
        ip = self.data['ip']
        return f'[{id(self)}:{ip}:({freq})]'

    def __str__(self):
        freq = self.data['freq']
        ip = self.data['ip']
        return f'[{id(self)}:{ip}:({freq})]'


class DoubleLinkedList:
    def __init__(self, max_length: int):
        self.len = 0
        self.max_length = max_length
        self.init: NodeItem = None
        self.last: NodeItem = None

    def __str__(self):
        values: list = []
        for node in self:
            pdb.set_trace()
            values.append(node)
        a_list = '|\n'.join(values)
        return f'[{a_list}]'

    def __iter__(self):
        node = self.init
        while node:
            current = node
            node = node.next
            yield current.value

    def is_empty(self):
        return self.init is None

    @staticmethod
    def is_intermediate(node: NodeItem) -> bool:
        return node.prev is not None and node.next is not None

    @staticmethod
    def should_swap(prev_node: NodeItem, current_node: NodeItem) -> bool:
        return prev_node.data['freq'] < current_node.data['freq']

    @staticmethod
    def is_disconnected(node: NodeItem):
        return node.prev is None and node.next is None

    def add_second(self, node: NodeItem):
        if DoubleLinkedList.should_swap(self.init, node):
            temp_node = self.init
            node.next = temp_node
            temp_node.prev = node
            temp_node.next = None
            self.init = node
            self.last = temp_node
            return 'append and replace second item'
        self.last = node
        self.init.next = node
        node.prev = self.init
        return 'append: second item'

    def increment(self):
        self.len = self.len + 1 if self.len < self.max_length else self.max_length

    def is_not_full(self):
        return self.len <= self.max_length

    def add(self, node: NodeItem) -> str:
        if self.init is None:  # first one
            self.init = node
            self.last = node
            node.prev = None
            node.next = None
            self.increment()
            return 'added: first elem'
        if self.init is not node and self.len == 1:  # 2 items
            second = self.add_second(node)
            self.increment()
            return f'added::{second}'
        if DoubleLinkedList.is_intermediate(node):  # intermediate node
            prev_node = node.prev
            next_node = node.next
            if DoubleLinkedList.should_swap(prev_node, node):
                node.prev = prev_node.prev
                if node.prev:
                    node.prev.next = node
                next_node.prev = prev_node
                prev_node.next = next_node
                prev_node.prev = node
                node.next = prev_node
                return 'added: intermediate elem'
            last_node = self.last
            if node is not self.last:
                node.prev = last_node
                last_node.next = node
                self.last = node
                return 'added: new elem'
        if DoubleLinkedList.is_disconnected(node):
            self.increment()
            last_node = self.last
            if self.is_not_full():
                if DoubleLinkedList.should_swap(last_node, node):
                    node.prev = last_node
                    last_node.next = node
                    self.last = node
                elif node is not self.last:
                    node.prev = last_node
                    last_node.next = node
                    self.last = node
                    return 'added: new elem'
                return 'added: last elem'
            # replace last element
            if DoubleLinkedList.should_swap(last_node, node):
                pre_last_node = last_node.prev
                node.prev = pre_last_node
                pre_last_node.next = node
                self.last = node
            # disconnect from list
            last_node.prev = None
            last_node.next = None
            return 'replaced: last elem'
        return 'end'

    def remove(self, node: NodeItem) -> NodeItem:
        if self.is_empty():
            return node
        if node is self.last:
            node.prev.next = None
        if node is self.init:
            node.next.prev = None
        else:
            # connect neighbors of node
            prev_node = node.prev  # temp
            next_node = node.next  # temp
            prev_node.next = next_node
            next_node.prev = prev_node
        # let the node full disconnected
        node.prev = None
        node.next = None
        return node

    def drop(self):
        node = self.last
        while node is not None:
            node.next = None
            node = node.prev
        self.init = None
        self.last = None

    def find(self, ip: str) -> NodeItem:
        node = self.init
        while node is not None:
            if node.data['ip'] == ip:
                return node
            node = node.next
        return None
