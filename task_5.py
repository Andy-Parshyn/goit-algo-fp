import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())# Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
    if node.left:
        graph.add_edge(node.id, node.left.id)
        l = x - 1 / 2 ** layer
        pos[node.left.id] = (l, y - 1)
        l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
    if node.right:
        graph.add_edge(node.id, node.right.id)
        r = x + 1 / 2 ** layer
        pos[node.right.id] = (r, y - 1)
        r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, node_size=2500, node_color=colors)
    plt.show()

def generate_tree(heap):
    nodes = [Node(val) for val in heap]
    for i in range(len(heap)):
        left_idx = 2*i+1
        right_idx = 2*i+2
        if left_idx < len(heap):
            nodes[i].left = nodes[left_idx]
        if right_idx < len(heap):
            nodes[i].right = nodes[right_idx]
    
    return nodes[0]

def generate_color(step, total_steps, base_color="#1296F0"):

    # Convert hex to RGB
    base_color = base_color.lstrip('#')
    r, g, b = tuple(int(base_color[i:i+2], 16) for i in (0, 2, 4))
    
    factor = step / max(total_steps - 1, 1)

    new_r = int(r + (255 - r) * factor)
    new_g = int(g + (255 - g) * factor)
    new_b = int(b + (255 - b) * factor)
    
    # Convert back to hex
    return f'#{new_r:02x}{new_g:02x}{new_b:02x}'

def bfs(root,size):
    if not root:
        return []
    
    queue = deque([root])
    visited = []
    step = 0
    
    while queue:
        node = queue.popleft()
        
        node.color = generate_color(step, size)
        visited.append(node)
        step += 1
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return visited

def dfs(root, size):
    if not root:
        return []
    
    stack = [root]
    visited = []
    step = 0
    
    while stack:
        node = stack.pop()
        node.color = generate_color(step, size)
        visited.append(node)
        step += 1
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return visited

# Створення дерева
heap = [14,90,7,34,76,2,32,78,11,8,42,51,20,17,3]
heapq.heapify(heap)
size = len(heap)
root = generate_tree(heap)

# BFS Обхід дерева
bfs(root,size)
draw_tree(root)

# DFS Обхід дерева
dfs(root,size)
draw_tree(root)
