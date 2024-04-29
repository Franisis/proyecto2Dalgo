"""
Fleury’s Algorithm for Eulerian Path

1. Make sure the graph has either 0 or 2 odd vertices.
2. If there are 0 odd vertices, start anywhere. If there are 2 odd vertices, start at one of them.
3. Follow edges one at a time. If you have a choice between a bridge and a non-bridge, always choose the non-bridge.
4. Stop when you run out of edges.
"""

from queue import Queue


def find_odd_vertex(graph):
    odd_vertex = None
    for node, neighbors in graph.items():
        if odd_vertex is None:
            odd_vertex = node
        if len(neighbors) % 2 == 1:
            odd_vertex = node
            break
    return odd_vertex


def bfs(v, u, graph):
    if len(graph[v]) > 0:
        visited = set()
        queue = Queue()
        queue.put(v)
        visited.add(v)
        while not queue.empty():
            current_node = queue.get()
            for next_node in graph[current_node]:
                if next_node == u:
                    return True
                if next_node not in visited:
                    queue.put(next_node)
                    visited.add(next_node)
        return False
    else:
        return True


def get_graph(dominos):
    graph = {}
    for domino in dominos:
        a = domino[0]
        b = domino[1]
        if a not in graph.keys():
            graph[a] = [b]
        else:
            graph[a].append(b)
        if b not in graph.keys():
            graph[b] = [a]
        else:
            graph[b].append(a)
    return graph


def es_posible(dominos):
    graph = get_graph(dominos)
    number_of_nodes = len(dominos)
    start_node = find_odd_vertex(graph)
    v = start_node
    path = []
    for i in range(number_of_nodes):
        neighbors = graph[v]
        found_next_node = False
        for u in neighbors:
            graph[v].remove(u)
            graph[u].remove(v)
            if bfs(v, u, graph):
                path.append((v, u))
                v = u
                found_next_node = True
                break
            else:
                graph[v].append(u)
                graph[u].append(v)
        if not found_next_node:
            return False
    return path

def conectar(dominos, n, w1, w2):
    x = es_posible(dominos)
    if not x:
        return 'NO SE PUEDE'
    else:
        return x

test_array = [(1, 1), (3, 1), (2, 1), (1, 3), (2, 2), (1, 2)]
test_array2 = [(1, 1), (3, 1), (2, 1), (1, 3), (4, 5), (1, 2)]
test_array3 = [(1,3), (-6,3), (1,7)]
test_array4 = [(1,2), (-2,3), (3, -4)]
print(conectar(test_array,0,0,0))
print(conectar(test_array2,0,0,0))
print(conectar(test_array3,0,0,0))
print(conectar(test_array4,0,0,0))