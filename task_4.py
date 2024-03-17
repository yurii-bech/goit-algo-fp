import uuid
import networkx as nx
import matplotlib.pyplot as plt

class HeapNode:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_heap_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_heap_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_heap_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_heap(heap_root):
    heap = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    heap = add_heap_edges(heap, heap_root, pos)

    colors = [node[1]['color'] for node in heap.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in heap.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(heap, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Функція для перетворення масиву в бінарну купу
def build_heap(array):
    def heapify(node, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(array) and array[left] > array[largest]:
            largest = left

        if right < len(array) and array[right] > array[largest]:
            largest = right

        if largest != index:
            array[index], array[largest] = array[largest], array[index]
            node.val, node.left.val, node.right.val = node.left.val, node.right.val, node.val
            heapify(node, largest)

    root = HeapNode(array[0])
    for i in range(1, len(array)):
        insert_node(root, HeapNode(array[i]))

    return root

def insert_node(node, new_node):
    queue = [node]
    while queue:
        current = queue.pop(0)
        if not current.left:
            current.left = new_node
            return
        elif not current.right:
            current.right = new_node
            return
        else:
            queue.append(current.left)
            queue.append(current.right)

# Створення бінарної купи та відображення
heap = build_heap([10, 5, 15, 20, 30, 8, 18])
draw_heap(heap)