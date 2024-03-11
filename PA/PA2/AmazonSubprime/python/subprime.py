# Tianze Ren, tr2bx, 02/10/2023, subprime.py
import heapq as pq

def dijkstras(capacity_graph, load_graph, start, end):
    for i in range(len(capacity_graph)):
        if len(capacity_graph[i]) != 0:
            for j in range(len(capacity_graph[i])):
                capacity_graph[i][j][1] = (load_graph[i][j][1]/capacity_graph[i][j][1])*100
    done = [False for node in capacity_graph]
    heap = []
    distance = [float('inf') for node in capacity_graph]
    distance[start] = 0
    pq.heappush(heap,(distance[start],start))
    parents = []
    for i in range(len(capacity_graph)):
        parents.append(-1)
    while len(heap)>0:
        current = pq.heappop(heap)
        current_node = current[1]
        current_dist = current[0]
        done[current_node] = True
        neighbors = capacity_graph[current_node]
        for item in neighbors:
            next_node = item[0]
            edge_weight = item[1]
            if edge_weight != 100:
                if not done[next_node]:
                    new_distance = current_dist + edge_weight
                    if new_distance < distance[next_node]:
                        parents[current_node] = next_node
                        distance[next_node] = new_distance
                        pq.heappush(heap, (new_distance,next_node))
    return parents

def subprime_path(capacity_graph, load_graph, start, end):
    parents = dijkstras(capacity_graph, load_graph, start, end)
    check = start
    path = [start]
    while parents[check] != -1:
        path.append(parents[check])
        check = parents[check]
    if path[len(path) - 1] != end:
        path.append(end)
    for i in range(len(path)):
        print(path[i])

def main():
    c = int(input())
    adjl_capacities = [[] for i in range(c)]
    adjl_loads = [[] for i in range(c)]
    for i in range(c):
        line = input().strip()
        if line.startswith('.'):
            continue
        pairs = line.split(';')
        for p in pairs:
            pair = p.split(',')
            adjl_capacities[i].append([int(pair[0]),int(pair[1])])
    for i in range(c):
        line = input().strip()
        if line.startswith('.'):
            continue
        pairs = line.split(';')
        for p in pairs:
            pair = p.split(',')
            adjl_loads[i].append([int(pair[0]),int(pair[1])])
    start = int(input())
    end=int(input())
    subprime_path(adjl_capacities,adjl_loads,start,end)
main()