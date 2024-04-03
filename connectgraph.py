def countCompleteComponents(n: int, edges: List[List[int]]) -> int:


    from collections import defaultdict

    def build_graph():
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return graph
    
    def dfs():
        pass


    def is_complete(components):
        size = len(components)
        expected_edge = size *(size -1) //2
        actual_edge =  sum(len(graph[node])) for node in component) // 2






    graph = build_graph()
    visited == [False] * n
    complete_components =  0 

    for i in range(n):
        if not visited[i]:
            components = dfs(i, visited, set())
            if is_complete(components):
                complete_components +=1





    graph = defaultdict(list)
    return 0


n = 6
edges = [[0, 1], [0, 2], [1, 2], [3, 4]]

output = coountCompleteComponents(n, edges)
k:
print(output)
