#Tianze Ren, tr2bx, donorcycle.py, 02/03/2023

dic = {}
def build_graph(match_scores, donor_friends):
    for i in range(len(match_scores)):
        dic[i] = []
        for j in range(len(match_scores[i])):
            if match_scores[i][j] > 60:
                if j not in dic[donor_friends[i]]:
                    dic[donor_friends[i]].append(j)



def isInCycle(match_scores,donor_friends,query):
    seen = []
    for i in range (len(dic)):
        seen.append(False)
    done = []
    for i in range (len(dic)):
        done.append(False)
    start = 0
    query_bool = False
    list1 = []
    return has_cycle_rec(dic, start, seen, done, query, query_bool,list1)


def has_cycle_rec(graph, curr, seen, done, query, query_bool,list1):
    cycle = False
    seen[curr] = True
    if curr == query:
        query_bool = True
    for v in graph[curr]:
        list1.append(curr)
        if seen[v] == True and done[v] == False and query_bool == True:
            list1.append(v)
            cycle = True
        elif seen[v] == False:
            cycle = has_cycle_rec(graph, v, seen, done, query, query_bool,list1)[1] or cycle
    done[curr] = True
    return list1, cycle

def take_input():
    n = int(input())
    m = int(input())
    donor_friends = input().split(',')
    for i in range(len(donor_friends)):
        donor_friends[i] = int(donor_friends[i])
    match_scores = []
    for i in range(m):
        match_row = input().split(',')
        for j in range(len(match_row)):
            match_row[j] = int(match_row[j])
        match_scores.append(match_row)
    query = int(input())
    build_graph(match_scores, donor_friends)
    retl,retb=isInCycle(match_scores, donor_friends, query)

    list2=[]
    for i in range(len(retl)-1):
        for j in range(i+1,len(retl)):
            if retl[i]==retl[j]:
                list2.append((i,j))

    final_result=False
    for indexes in list2:
        if query in retl[indexes[0]:indexes[1]+1]:
            final_result=True
            break

    if retb:
        print(final_result)
    else:
        print(retb)

take_input()





