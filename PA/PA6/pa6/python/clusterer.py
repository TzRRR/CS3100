import heapq as pq

def cluster_cost(k, distances):
    node_set = {0}
    MST = []
    new_node = 0
    while len(MST) < (len(distances) - 1):
        minimum = float("inf")
        for i in node_set:
            for j in range (0, len(distances[i])):
                if distances[i][j] < minimum and (j not in node_set):
                    minimum = distances[i][j]
        for m in node_set:
            for l in range (0, len(distances[m])):
                if distances[m][l] == minimum and (l not in node_set):
                    new_node = l
        node_set.add(new_node)
        MST.append(minimum)

    MST.sort(reverse = True)
    print(MST[k - 2])
