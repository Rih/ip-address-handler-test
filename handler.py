

class NodeItem:
    def __init__(self, ip: str):
        self.data: dict = {
            'freq': 1,
            'ip': ip,
        }
        self.prev: NodeItem = None
        self.next: NodeItem = None


class NodeHeap:
    def __init__(self):
        self.ips: DoubleLinkedList = DoubleLinkedList()
        self.prev: NodeHeap = None
        self.next: NodeHeap = None
    
    def is_last(self):
        return self.next is None
    
    def is_first(self):
        return self.prev is None


class DoubleLinkedList:
    def __init__(self):
        self.init: NodeItem = None
    

class HeapTree:
    def __init__(self):
        self.parent: NodeHeap = None
        self.root: NodeHeap = None
        self.left: NodeHeap = None
        self.right: NodeHeap = None
        
    def is_empty(self):
        return self.root is None
    
    def add(self, node: NodeHeap):
        if self.root is None:
            self.root = node
            return True
        
    
ips = {
    '1.1.1.1': {
        'freq': 1,
        'node': NodeItem('1.1.1.1'),
    },
    '1.1.1.2': {
        'freq': 1,
    }
}

heap = HeapTree()


def find_node(node: NodeItem, data: dict) -> NodeItem:
    while node.freq != data['freq']:
        if node.freq < data.freq:
            node = node.left
        else:
            node = node.right
    return node


def request_handled(ip_address: str):
    print(f'{ip_address}')
    data = ips[ip_address]
    node = find_node(heap.root.data, data)
    data['pos'] = len(node.ips) + 1
    node.ips.append(ip_address)


def top100():
    pass


def clear():
    ips = {}
    heap = Heap()


if __name__ == '__main__':
    ips = 20_000_000
    for ip in range(ips):
        request_handled('1.1.1.1')


