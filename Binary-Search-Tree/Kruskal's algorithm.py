def kruskal(graph):
    mst = []
    edges = []
    for node in graph:
        for neighbor, weight in graph[node].items():
            edges.append((weight, node, neighbor))
    edges.sort()
    parent = {node: node for node in graph}
    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]
    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)
        if root1 != root2:
            parent[root2] = root1
    for weight, node1, node2 in edges:
        if find(node1) != find(node2):
            mst.append((node1, node2, weight))
            union(node1, node2)
    return mst
