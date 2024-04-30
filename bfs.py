from collections import deque

def bfs(graph, start, target):
    visited = set()
    queue = deque([(start,[start])])
    visited.add(start)
    traversal = []
    traversal.append(start)

    while queue:
        current_node, path = queue.popleft()
        if current_node==target:
            print("Traversal Path: "," -> ".join(traversal))
            return path
        
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                traversal.append(neighbor)
                queue.append((neighbor, path+[neighbor]))
    return None


graph = {
    'A':['B','D','E'],
    'B':['A','C','E'],
    'C':['B','E','F','G'],
    'D':['A','E'],
    'E':['A','B','C','D','F'],
    'F':['E','C','G'],
    'G':['C','F']
}

start_node = 'A'
target_node = 'G'

print("Breadth First Search")
path = bfs(graph, start_node, target_node)

if path:
    print(f"Path from {start_node} to {target_node} is: "," -> ".join(path))