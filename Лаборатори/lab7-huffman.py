import heapq
from collections import Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def huffman_tree(char_freqs):
    heap = []
    for char, freg in char_freqs.items():
        heapq.heappush(heap, Node(char,freg))
        
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]

def print_tree(node,prefix=""):
    if node is not None:
        if node.char is not None:
            print(f"{node.char}: {node.freq} - {prefix}")
        print_tree(node.left, prefix+"0")
        print_tree(node.right, prefix+"1")


char_freqs = {
    'A': 5,
    'B': 9,
    'C': 12,
    'D': 13,
    'E': 16,
    'F': 45
}

codes = huffman_tree(char_freqs)
print_tree(codes)

