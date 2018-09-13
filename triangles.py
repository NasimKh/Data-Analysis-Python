from pyspark import SparkConf, SparkContext
import sys
import itertools

##two arguments, input and output

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

#keys = data_s.map(lambda y: (int(y[0]), y[1:]))
keys = data_s.map(lambda y: (y[0], y[1:]))
vals = keys.map(lambda y: y[1])


combos = keys.map(lambda k: (k[0],list(itertools.combinations(k[1],2))))

#combos_add = combos.map(lambda x: (lambda i: i + (x[0],))x)
combos_add = combos.map(lambda t: [(t[0],)+i*1 for i in t[1]])
triangles = combos_add.flatMap(lambda x: x)
#triangles_s = triangles.map(lambda x: tuple(sorted(x, key = lambda x:float(x))))
triangles_s = triangles.map(lambda x: tuple(sorted(x, key = lambda x:x)))
#triangles_s2 = triangles.map (lambda x: [x for i in sorted(x[0])])

## add 1 to end of each tuple for counting purposes
#triangles_1 = triangles_s.map(lambda y: (y,1))
#triangles_kc = triangles_1.countByKey()


##make everything in sorted tuples into integers
#triangles_int = triangles_s.map(lambda i: [int(j) for j in i])
##Add 1 to these tuples
#triangles_tup = triangles_int.map(lambda x: (tuple(x),1))
triangles_tup = triangles_s.map(lambda x: (tuple(x),1))

triangles_gr = triangles_tup.reduceByKey(lambda x,y: x + y)
triangles_filter = triangles_gr.filter(lambda x: x[1] >1)
triangles_final = triangles_filter.map(lambda x: x[0])



#triangles_kc_int = triangles_tup.countByKey()

#triangles_friends_dict = {k: v for k,v in triangles_kc_int.items() if v > 1}
#triangles_friends = triangles_friends_dict.keys()
##So now how to put this into a txt file??
#final_triangles = sc.parallelize(triangles_friends)

##save in specificed output directory
triangles_final.saveAsTextFile(outputlocation)
sc.stop()