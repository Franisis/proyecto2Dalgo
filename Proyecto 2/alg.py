from queue import Queue
from LTP import calculate_ltp

def getGraph(fundamentals,w1,w2):
    graph={}
    for fundamental in fundamentals:
        for fundamental1 in fundamentals:
            
                fundamentalA=fundamental[0]
                fundamentalB=fundamental[1]
                fundamental1A=fundamental1[0]
                fundamental1B=fundamental1[1]
                fafb = calculate_ltp(fundamentalA,fundamentalB,w1,w2)
                fa1fb = calculate_ltp(fundamental1A, fundamentalB,w1,w2)
                fafb1=calculate_ltp(fundamentalA, fundamentalB,w1,w2) 
                if fundamentalA not in graph.keys():    
                    graph[fundamentalA]=[{fundamentalB:fafb},{fundamental1B:fafb1}] #atom:pesoArco
                    graph[-fundamentalA]=[{fundamentalB:fafb},{fundamental1B:fafb1}] #atom:pesoArco
                else:
                    graph[fundamentalA].append({fundamentalB:fafb})
                    graph[fundamentalA].append({fundamental1B:fafb1})

                    graph[-fundamentalA].append({fundamentalB:fafb})
                    graph[-fundamentalA].append({fundamental1B:fafb1})
                if fundamentalB not in graph.keys():    
                    graph[fundamentalB]=[{fundamentalA:fafb},{fundamental1A:fa1fb}] #atom:pesoArco
                    graph[-fundamentalB]=[{fundamentalA:fafb},{fundamental1A:fa1fb}] #atom:pesoArco
                else:
                    graph[fundamentalB].append({fundamentalA:fafb})
                    graph[fundamentalB].append({fundamental1A:fa1fb})

                    graph[-fundamentalB].append({fundamentalA:fafb})
                    graph[-fundamentalB].append({fundamental1A:fa1fb})
    return graph
                    
def find_odd_vertex(graph):
    odd_vertex=None
    for node,neighbors in graph.items():
        if odd_vertex is None:
            odd_vertex = node
        if len(neighbors) %2 == 1:
            odd_vertex= node
            break
    return odd_vertex

def bfs(v,u,graph):
    if len(graph[v])>0:
        visited = set() #conjunto
        queue = Queue() #cola
        queue.put(v)
        visited.add(v)
        while not queue.empty():
            current_node = queue.get()
            for next_node in graph[current_node]:
                next_node=removeFromGraph(next_node)
                if next_node == u:
                    return True
                if next_node not in visited:
                    queue.put(next_node)
                    visited.add(next_node)
        return False
    else:
        return True

def es_posible(fundamentals,w1,w2):
    graph = getGraph(fundamentals,w1,w2)
    number_of_nodes = len(fundamentals)
    start_node = find_odd_vertex(graph)
    v = start_node
    path=[]
    for i in range(number_of_nodes):
        neighbors = graph[v]
        found_next_node = False
        for u in neighbors:
            u=removeFromGraph(u)
            v=removeFromGraph(v)
            if u in graph[v]:
                graph[v].remove(u)
            if v in graph[u]:
                graph[u].remove(v)
            if bfs(v,u,graph):
                if u != v:
                    path.append((v,u))
                v=u
                found_next_node = True
                break
            else:
                graph.append(u)
                graph.append(v)
        if not found_next_node:
            return "NO SE PUEDE"
    return path
def get_key(u,val):
    for key, value in u.items():
        if val == value:
            return key

def removeFromGraph(u):
    key = None
    if type(u)==dict:
        key=(list(u.keys())[0])
    if type(u)==int:
        key=u
    return key