from Util import scatter_plot
import time
from collections import deque
import sys
import gc


def getClusterArr(file):
    cluster_dic = {}
    node_set = set()
    f = open(file,"r")
    lines = f.readlines()
    for l in lines:
        try:
            a,b = l.strip().split()
            a,b = int(a),int(b)
            node_set.add(a)
            node_set.add(b)
            if a in cluster_dic:
                cluster_dic[a].add(b)
            else:
                cluster_dic[a] = set()
                cluster_dic[a].add(b)

        except:
            pass

    print(sys.getsizeof(lines))
    print(sys.getsizeof(cluster_dic))
    print(sys.getsizeof(node_set))
    del lines
    gc.collect()
    diameterDist = {}
    sample_num = 100000000
    num = 0
    print("shuai")
    for node in node_set:
        num+=1
        if num>sample_num:break

        q = deque()
        s = set()
        q.append(node)
        s.add(node)
        dia = -1
        while len(q)!=0:
            l = len(q)
            dia += 1
            for i in range(l):
                diameterDist[dia] = diameterDist.get(dia,0)+1
                tem = q.popleft()
                if tem in cluster_dic:
                    for n in cluster_dic[tem]:
                        if n not in s:
                            q.append(n)
                            s.add(n)

    numerator = 0
    denominator = 0
    for x,y in diameterDist.items():
        numerator += x*y
        denominator += y
    return diameterDist,numerator,denominator

def getDiameterfPic(file,dataName):
    diameterDist, numerator, denominator = getClusterArr(file)
    dia = list(diameterDist.keys())
    count = list(diameterDist.values())
    scatter_plot(dia, count, "distance", "count", "diameter-" + dataName, "result/diameter-" + dataName + ".png")
    print(numerator)
    print(denominator)
    print("res:"+str(numerator/denominator))
if __name__ == "__main__":
    start = time.time()
    getDiameterfPic("data/wiki-Vote.txt","wiki-Vote")
    end = time.time()
    print(end-start)