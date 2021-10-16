import random
from structures import (
    NodeItem,
    NodeHeap,
    HeapTree,
    DoubleLinkedList,
)
import pdb

'''ips = {
    '1.1.1.1': {
        'freq': 1,
        'node': NodeItem('1.1.1.1'),
    },
    '1.1.1.2': {
        'freq': 1,
        'node': NodeItem('1.1.1.2'),
    }
}'''

ips = {}
top100 = DoubleLinkedList()
heap = HeapTree()


def request_handled(ip_address: str):
    print(f'trying: {ip_address}')
    if ips.get(ip_address):
        data = ips[ip_address]
        node_heap = heap.find_or_create_node(ips[ip_address])
        node_item = ips[ip_address]['node']
        same_node_item = node_heap.ips.remove(node_item)
        ips[ip_address] = {
            'freq': data['freq'] + 1,
            'node': same_node_item,
        }
        node_heap = heap.find_or_create_node(node_heap, ips[ip_address])

        added = node_heap.ips.add(ip_address, data['freq'] + 1)
    else:
        freq = 1  # first hit
        node_heap = NodeHeap(freq)
        node = NodeItem(ip_address, freq)
        ips[ip_address] = {'freq': freq, 'node': node}
        node_heap.ips.add(node)
        heap.add()
        print(node_heap.ips)
    print(node)


def top100():
    pass


def clear():
    global ips, heap
    ips = {}
    heap = HeapTree()


if __name__ == '__main__':
    # total_ips = 20_000_000
    total_ips = 20
    for ip in range(total_ips):
        octet = random.randint(1, 5)
        request_handled(f'1.1.1.{octet}')
        input('next: ')
        print(ips)


