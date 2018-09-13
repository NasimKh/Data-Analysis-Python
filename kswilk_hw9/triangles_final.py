from pyspark import SparkConf, SparkContext
import sys
import itertools


if len(sys.argv) != 3:
    print('Usage: ' + sys.argv[0] + ' <in> <out>')
    sys.exit(1)

inputlocation = sys.argv[1]
outputlocation = sys.argv[2]

conf = SparkConf().setAppName('triangles')
sc = SparkContext(conf = conf)

##read in data
data = sc.textFile(inputlocation)

##first but into ascii characters
##then split on line
data_as = data.map(lambda x: x.encode('ascii'))
data_s = data_as.map(lambda line: line.split())

# split data into key (first value) and values (rest of the values)
keys = data_s.map(lambda y: (y[0], y[1:]))
vals = keys.map(lambda y: y[1])

#use itertools.combinations to create all the different combinations for the values for a given key
combos = keys.map(lambda k: (k[0],list(itertools.combinations(k[1],2))))

#Put key into combination tuples
combos_add = combos.map(lambda t: [(t[0],)+i*1 for i in t[1]])

#flatten so now each value in list is a tuple of 3
triangles = combos_add.flatMap(lambda x: x)

##sort the tuples so we don't double count
triangles_s = triangles.map(lambda x: tuple(sorted(x, key = lambda x:x)))

#add 1 outside of each tuple so we can count each tuple
triangles_tup = triangles_s.map(lambda x: (tuple(x),1))

#Reduce by counting each by the key (the triangle tuple)
triangles_gr = triangles_tup.reduceByKey(lambda x,y: x + y)

#filter to where the tuple count >1. That is, the triple tuple appears more than once
triangles_filter = triangles_gr.filter(lambda x: x[1] >1)
#Final output is just the triangles
triangles_final = triangles_filter.map(lambda x: x[0])


triangles_final.saveAsTextFile(outputlocation)
sc.stop()
