# coding: utf-8
from copy import copy, deepcopy


class Node(object):

    def __init__(self, value=None, nodes=[]):
        self.value = value
        self.nodes = nodes
        self.deepness = 0
        self.parent = None

    def add_node(self, node):
        node.parent = self
        self.nodes.append(node)

    def __repr__(self):
        return f"({self.value}), {len(self.nodes)} nodes"


def tree(node, arr):

    if len(arr) == 1:
        return
    else:
        head = node.value
        arr.pop(arr.index(head))
        node.value = head

        for i in arr:
            node.add_node(Node(i, []))

        for n in node.nodes:
            newarr = copy(arr)
            tree(n, newarr)
        return

def get_combination(node, code: str) -> [str]:
    parsed_code = code.split('-')
    if len(node.nodes) == 0:
        return [str(node.value)]
    else:
        num = int(parsed_code[0]) % len(node.nodes)
        new_node = node.nodes[num]
        val = get_combination(new_node, '-'.join(parsed_code[1:]))
        return [str(node.value)] + val

from math import floor
def get_combination_from_genome(node, genome, length):
    genome_len = len(genome)
    code_len = floor(genome_len/(length-1))
    code = []
    for i in range(length):
        cad = genome[i:i+code_len]
        cadsum = sum(cad)
        code.append(str(cadsum))
    comb = get_combination(node, "-".join(code))
    return comb

def main():

    A, B, C, D, E, F = "A", "B", "C", "D", "E", "F"
    arr = [A, B, C, D, E, F]
    node = Node(A)
    tree(node, arr)

    print(node)
    comb = get_combination(node, "12-34-56-78-90")
    # comb = get_combination_from_genome(node, [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0], len(arr))
    print(comb)


if __name__ == '__main__':
    main()
