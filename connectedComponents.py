from Util import scatter_plot
import time
from collections import deque

def getComponentArr(file):
    cluster_dic = {}
    f = open(file,"r")
    lines = f.readlines()
    for l in lines:
        a,b = l.strip().split()
        a,b = int(a),int(b)
        edge = str(a)+","+str(b)
        if a in cluster_dic:
            cluster_dic[a].add(b)
        else:
            cluster_dic[a] = set()
            cluster_dic[a].add(b)

        if b in cluster_dic:
            cluster_dic[b].add(a)
        else:
            cluster_dic[b] = set()
            cluster_dic[b].add(a)

    nodeList = list(cluster_dic.keys())
    nodeSet = set()
    q = deque()
    componentDis = []
    for node in nodeList:
        if node not in nodeSet:
            q.append(node)
            num = 1
            nodeSet.add(node)
            while len(q)!=0:
                tem = q.popleft()
                for x in cluster_dic[tem]:
                    if x not in nodeSet:
                        nodeSet.add(x)
                        q.append(x)
                        num += 1

            componentDis.append(num)
    return componentDis

def getComponentPic(file,dataName):
    componentDis = getComponentArr(file)
    print(sum(componentDis))
    numDic = {}
    for x in componentDis:
        numDic[x] = numDic.get(x,0)+1
    x = list(numDic.keys())
    y = list(numDic.values())
    print(numDic)
    scatter_plot(x, y, "component size", "Count", "connected Component-" + dataName, "result/connected Component-" + dataName + ".png")

if __name__ == "__main__":
    start = time.time()
    getComponentPic("data/kronecker.txt","kronecker")
    end = time.time()
    print(end - start)




