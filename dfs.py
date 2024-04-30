def dfs(graph, start, target):
    visited = set()
    traversal = []
    stack = [(start,[start])]
    while stack:
        current_node, path = stack.pop()
        traversal.append(current_node)
        if current_node==target:
            print("Traversal Path: ",' -> '.join(traversal))
            return path
        if current_node not in visited:
            visited.add(current_node)
            neighbors = sorted(set(graph[current_node])-visited, reverse=True)
            for neighbor in neighbors:
                stack.append((neighbor, path+[neighbor]))
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

print("\nDepth First Search")

path = dfs(graph, start_node, target_node)

if path:
    print("Path is: "," -> ".join(path))