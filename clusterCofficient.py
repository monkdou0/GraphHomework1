from Util import scatter_plot
import time
import sys
import gc



def getClusterArr(file):
    in_dic = {}
    out_dic = {}
    f = open(file,"r")
    lines = f.readlines()
    for l in lines:
        try:
            a,b = l.strip().split()
            a,b = int(a),int(b)
            edge = str(a)+","+str(b)

            if a in out_dic:
                out_dic[a].add(b)
            else:
                out_dic[a] = set()
                out_dic[a].add(b)

            if b in in_dic:
                in_dic[b].add(a)
            else:
                in_dic[b] = set()
                in_dic[b].add(a)
        except:
            pass


    degree = []
    coefficient = []
    print(sys.getsizeof(lines))
    print(sys.getsizeof(in_dic))
    print(sys.getsizeof(out_dic))

    sample_num = 10
    num = 0
    for x,out_set in out_dic.items():
        num +=1
        if num>sample_num: break
        print(num)
        if x in in_dic:
            in_set = in_dic[x]
        else:
            in_set = set()

        union_set = out_set.union(in_set)

        if len(union_set)==1:
            degree.append(1)
            coefficient.append(0)
        else:
            numerator = 0
            for node1 in union_set:
                for node2 in union_set:
                    if node2!=node1:
                        numerator += (1 if node2 in out_dic[node1] else 0)
            denominator = len(union_set)*(len(union_set)-1)
            degree.append(len(union_set))
            coefficient.append(numerator/denominator)
            print(str(degree)+str(coefficient))

    aver_coeff = sum(coefficient)/len(coefficient)

    return degree,coefficient,aver_coeff

def getClusterCoefPic(file,dataName):
    degree, coefficient, aver_coeff = getClusterArr(file)
    scatter_plot(degree, coefficient, "k(degree)", "c(cluster coefficient)", "cluster coefficient-" + dataName, "result/cluster coefficient-" + dataName + ".png")
    print(len(degree))
    print(aver_coeff)

if __name__ == "__main__":
    start = time.time()
    getClusterCoefPic("data/big.txt","friendster")
    end = time.time()
    print(end-start)