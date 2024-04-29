from queue import Queue
from LTP import calculate_ltp


def getGraph(fundamentals, w1, w2):
    graph = {}
    for fundamental in fundamentals:
        a = int(fundamental[0])
        b = int(fundamental[1])
        TLPa=(a,calculate_ltp(a,b,w1,w2))
        TLP_a=(-a,calculate_ltp(-a,b,w1,w2))
        TLPb=(b,calculate_ltp(a,b,w1,w2))
        TLP_b=(-b,calculate_ltp(a,-b,w1,w2))
        if a not in graph.keys():
            graph[a]=[(b,calculate_ltp(a,b,w1,w2))]
            graph[-a]=[(b,calculate_ltp(-a,b,w1,w2))]
            graph[TLPa[0]]=[(b,TLPa[1])]
            graph[TLP_a[0]]=[(b,TLP_a[1])]

        else:
            graph[a].append((b,calculate_ltp(a,b,w1,w2)))
            graph[-a].append((b,calculate_ltp(a,b,w1,w2)))
            graph[TLP_a[0]].append((b,TLP_a[1]))
            graph[TLPa[0]].append((b,TLP_a[1]))
            
        if b not in graph.keys():
            graph[b]=[(a,calculate_ltp(a,b,w1,w2))]
            graph[-b]=[(a,calculate_ltp(-a,b,w1,w2))]
            graph[TLPb[0]]=[(a,TLPb[1])]
            graph[TLP_b[0]]=[(a,TLP_b[1])]
            

        else:
            graph[b].append((a,calculate_ltp(a,b,w1,w2)))
            graph[-b].append((a,calculate_ltp(a,b,w1,w2)))
            graph[TLP_b[0]].append((a,TLP_b[1]))
            graph[TLPb[0]].append((a,TLP_b[1]))

    return graph 

def findOddVertex(graph):
    oddVertex=None
    for node, neighbors in graph.items():
        if oddVertex is None:
            oddVertex= node
        if len(neighbors)%2==1:
            oddVertex = node
            break
    return oddVertex

def bfs(v, u , graph):
    if len(graph[v])>0:
        visited=set()
        queue=Queue()
        queue.put(v)
        visited.add(v)
        while not queue.empty():
            current_node = queue.get()
            if type(current_node)==tuple:
                current_node=queue.get()[0]
            for next_node in graph[current_node]:
                if next_node == u:
                    return True
                if next_node not in visited:
                    queue.put(next_node)
                    visited.add(next_node)
        return False
    else:
        return True
    
            
def es_posible(fundamentals,w1,w2):
    graph=getGraph(fundamentals,w1,w2)
    numberOfNodes = len(graph)
    startNode = findOddVertex(graph)
    v= startNode
    path=[]
    for i in range(numberOfNodes):
        neighbors = graph[v]
        found_next_node= False
        for u in neighbors:
            up = u
            u=u[0]
            graph[v].remove(up)
            graph[u].remove((v,calculate_ltp(u,v,w1,w2)))
            if bfs(v,u,graph):
                path.append((v,u))
                v=u
                found_next_node=True
                break
            else:
                graph[v].append(u)
                graph[u].append(v)
        if not found_next_node:
            return "NO SE PUEDE"
    return path