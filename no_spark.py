from pyspark import SparkContext
import random

sc = SparkContext(appName="Demo")

random_ints = [random.randint(0,100) for _ in range(1000)]
rdd = sc.parallelize(random_ints)

rdd1 = rdd.map(lambda a: (a, 1))
rdd2 = rdd1.reduceByKey(lambda a, b: a + b)
rdd3 = rdd2.sortBy(lambda x: x[0])

# Remove the spark lines
# res = rdd3.collect()

# and the dependency on spark
for item in []:
    print("DEMO RESULT: {:<5}\t{}".format(item[0],item[1]))
