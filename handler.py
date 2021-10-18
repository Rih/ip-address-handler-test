import random
from structures import (
    NodeItem,
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
MAX_LENGTH = 5
top_ips = DoubleLinkedList(MAX_LENGTH)


def request_handled(ip_address: str):
    print(f'receiving: {ip_address}')
    if ips.get(ip_address):
        data = ips[ip_address]
        node_item = ips[ip_address]['node']
        ips[ip_address] = {
            'freq': data['freq'] + 1,
            'node': node_item,
        }
        add_text = top_ips.add(node_item)
        node_item.data['freq'] = ips[ip_address]['freq']
        print(add_text)
        return
    # new one
    freq = 1  # first hit
    node_item = NodeItem(ip_address, freq)
    ips[ip_address] = {'freq': freq, 'node': node_item}
    add_text = top_ips.add(node_item)
    print(add_text)


def top100():
    tops = [v for v in top_ips]
    print('[\n' + ';\n'.join(tops) + '\n]')
    return tops


def clear():
    global top_ips, ips
    ips = {}
    top_ips.drop()


if __name__ == '__main__':
    # total_ips = 20_000_000
    total_ips = 10
    for ip in range(total_ips):
        octet = random.randint(1, 15)
        request_handled(f'1.1.1.{octet}')
        for k, v in ips.items():
            print(f'ip: {k} -> freq: {v["freq"]}')
    top100()
