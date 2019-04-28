from pyspark import SparkContext
import random

sc = SparkContext(appName="Demo")

random_ints = [random.randint(0,100) for _ in range(1000)]

print("JEROEN EOF")
