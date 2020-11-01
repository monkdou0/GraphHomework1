from Util import scatter_plot
import time

in_degree = {}
out_degree = {}
node_set = set()

def getDegree(file):
    f = open(file,"r")
    lines = f.readlines()
    for l in lines:
        try:
            a,b = l.strip().split()
            a,b = int(a),int(b)
            in_degree[b] = in_degree.get(b,0)+1
            out_degree[a] = out_degree.get(a,0)+1
            node_set.add(a)
            node_set.add(b)
        except:
            pass
    return in_degree,out_degree,node_set

def getDegreeDistribution(dic):
    count = {}
    for x, y in dic.items():
        count[y] = count.get(y, 0) + 1

    key = list(count.keys())
    value = list(count.values())
    return key,value

def getDegreeDisPic(file,dataName):
    in_degree,out_degree,node_set = getDegree(file)
    in_key,in_value = getDegreeDistribution(in_degree)
    scatter_plot(in_key, in_value, "in_degree", "count", "in_degree_distribution-"+dataName, "result/in_degree_distribution-"+dataName+".png")
    out_key, out_value = getDegreeDistribution(out_degree)
    scatter_plot(out_key, out_value, "out_degree", "count", "out_degree_distribution-" + dataName, "result/out_degree_distribution-" + dataName + ".png")
    for i in range(65608366):
        if i not in node_set:
            print(i)
if __name__ == "__main__":
    start = time.time()
    file = "data/big.txt"
    dataName = "friendster"
    getDegreeDisPic(file,dataName)
    end = time.time()
    print(end-start)






