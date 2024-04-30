#Diana Carolina Salazar Velandia
# Counting the 10 most popular words, task of presentation Big_data_4
import sys
import heapq
from operator import add
from heapq import nlargest
from pyspark import SparkContext


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print >> sys.stderr, "Usage: pyspark <python script> <file>"
        exit(-1)
    sc = SparkContext(appName="PythonWordCount")
    lines = sc.textFile(sys.argv[1], 1)
    counts = lines.flatMap(lambda x: x.split(' ')).map(lambda x: (x, 1)).reduceByKey(add)
    output = counts.sortBy(lambda x: x[1]).collect()
    
    f = open("wc10.txt", "w")
    N = 10
    res = output[-N:]
    
    for (word, count) in res:
        f.write("%s: %i\n" % (word, count))

    f.close()
    
    sc.stop()
