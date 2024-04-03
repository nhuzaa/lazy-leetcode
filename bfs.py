from collections import deque


def bfs(graph, S):
    queue = deque(S)
    visited = set()

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)

            queue.extend(n for n in graph[vertex] if n not in visited)


if __name__ == "__main__":
    # Graph represented as a dictionary
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }
    bfs(graph, "C")
