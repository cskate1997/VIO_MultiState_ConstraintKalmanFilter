import sys
class Pair:
    def __init__(self,first,second):
        self.first = first
        self.second = second

# infini = sys.maxsize

class Node:

    def __init__(self,vertexNumber):
        self.vertexNumber = vertexNumber
        self.children = []


    def Add_child(self, vNumber, length):
        p = Pair(vNumber,length)
        self.children.append(p)

def DijkstraDist(g,s,path):

    dist = [sys.maxsize] * len(g)
    # print(len(dist))
    visited = [False] * len(g)

    for i in range(len(g)):
        path[i] = -1

    dist[s] = 0
    path[s] = -1
    current = s

    sett = set()

    while True:
        visited[current] = True
        print(g[current].children[0].second)
        # while True:
        #     pass
        for i in range(len(g[current].children)):
            v = g[current].children[i].first
            if visited[v]:
                continue

            sett.add(v)
            alt = dist[current] + g[current].children[i].second

            if alt < dist[v]:
                dist[v] = alt
                path[v] = current
        if current in sett:
            sett.remove(current)
        if (len(sett) == 0):
            break

        minDist = sys.maxsize
        index = 0

        for a in sett:
            if dist[a] < minDist:
                minDist = dist[a]
                index = a
        current = index

    return dist

# def printpath(path, i, s):
#     if i !=s:
#         if path[i] == -1:
#             print("Path not Found!!")
#             return
#         printpath(path, path[i], s)
#         print(path[i] + "")

def min_length(n, fr, to, weight):
    l = []
    m = len(fr)

    for a in range(n):
        v = []
        src = a

        for i in range(n+1):
            d = Node(i)
            v.append(d)

        for j in range(m):

            if to[j] == src + 1:
                v[fr[j]-1].Add_child(n,weight[j])
            else:
                v[fr[j]-1].Add_child(to[j]-1, weight[j])

        path = [0] * len(v)
        dist = DijkstraDist(v, src, path)

        if dist[-1] == sys.maxsize:
            l.append(0)
        else:
            l.append(dist[-1])
    print(l)

if __name__ == '__main__':

    n = 4
    fr = [1,3,2,4,1]
    to = [3,2,1,2,4]
    wts = [20,25,12,15,10,5]

    min_length(n,fr,to,wts)
