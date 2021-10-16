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
    def __init__(self):
        self.init: NodeItem = None
        self.last: NodeItem = None

    def __str__(self):
        values: list = []
        node = self.init
        while node is not None:
            values.append(node.value)
        return '|'.join(values)

    def is_empty(self):
        return self.init is None

    def add(self, node: NodeItem) -> NodeItem:
        if self.init is None:  # first one
            self.init = node
            self.last = node
        else:
            node.prev = self.last
            self.last.next = node
        return node

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

    def find(self, ip: str) -> NodeItem:
        node = self.init
        while node is not None:
            if node.data['ip'] == ip:
                return node
            node = node.next
        return None


class NodeHeap:
    def __init__(self, freq: int = 1):
        self.ips: DoubleLinkedList = DoubleLinkedList()
        self.freq = freq
        self.root: NodeHeap = None
        self.parent: NodeHeap = None
        self.left: NodeHeap = None
        self.right: NodeHeap = None

    def is_leaf(self):
        return self.next is None and self.prev is None


class HeapTree:
    def __init__(self):
        self.root: NodeHeap = None

    def is_empty(self):
        return self.root is None

    def insert(self, node: NodeHeap):
        pass

    def add(self, ip: str, new_freq: int):
        if self.root is None:
            self.root = NodeHeap(new_freq)
            node = self.root.ips.add(ip, new_freq)
            return True
        node = HeapTree.find_node(self.root, new_freq)
        if node is None:
            node_heap = NodeHeap(new_freq)

    def find_or_create_node(self, data: dict) -> NodeHeap:
        node = self.root
        if not node:
            self.root = NodeHeap(data['freq'])
            return self.root
        while node and node.freq != data['freq']:
            if node.freq < data['freq']:
                node = node.left
            else:
                node = node.right
        return node
