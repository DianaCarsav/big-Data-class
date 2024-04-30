#Diana Carolina Salazar Velandia
# Counting the number of all lines, task of presentation Big_data_4
import sys
from operator import add

from pyspark import SparkContext

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print >> sys.stderr, "Usage: pyspark <python script> <file>"
        exit(-1)
    sc = SparkContext(appName="PythonWordCount")
    lines = sc.textFile(sys.argv[1], 1)
    counts = lines.flatMap(lambda x: x.split('\n')).map(lambda x: (x, 1)).reduceByKey(add)
    output = counts.sortBy(lambda x: x[0]).collect()
    f = open("wclines.txt", "w")
    suma = 0
    for (word, count) in output:
        suma += count
    f.write("Total Number of lines: " + str(suma))
    #for (word, count) in output:
    #    f.write("%s: %i\n" % (word, count))
    f.close()

    sc.stop()