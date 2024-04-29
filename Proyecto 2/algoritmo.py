from queue import Queue
from LTP import calculate_ltp


def find_odd_vertex(graph):
    odd_vertex = None
    for node, neighbors in graph.items():
        if odd_vertex is None:
            odd_vertex = node
        if len(neighbors) % 2 == 1:
            odd_vertex = node
            break
    return odd_vertex


def get_graph(fundamentals):
    graph = {}
    for domino in fundamentals:
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

def es_posible(fundamentals):
    graph = get_graph(fundamentals)
    number_of_nodes = len(fundamentals)
    start_node = find_odd_vertex(graph)
    v = start_node
    path = []
    for i in range(number_of_nodes):
        neighbors = graph[v]
        found_next_node = False
        for u in neighbors:
            print(u)
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
            return "NO SE PUEDE"
    return path
