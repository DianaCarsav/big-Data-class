#Diana Carolina Salazar Velandia
# Counting the number of all words, task of presentation Big_data_4
import sys
from operator import add

from pyspark import SparkContext

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print >> sys.stderr, "Usage: pyspark <python script> <file>"
        exit(-1)
    sc = SparkContext(appName="PythonWordCount")
    lines = sc.textFile(sys.argv[1], 1)
    counts = lines.flatMap(lambda x: x.split(' ')).map(lambda x: (x, 1)).reduceByKey(add)
    output = counts.sortBy(lambda x: x[0]).collect()
    f = open("wcCW.txt", "w")
    suma = 0
    for (word, count) in output:
        suma += count
    f.write("Total Number of words: " + str(suma))
    f.close()

    sc.stop()
