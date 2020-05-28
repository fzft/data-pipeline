from operator import add
from random import random

from pyspark.sql import SparkSession


def analyze(spark: SparkSession):
    partitions = 1
    n = 1 * partitions

    def f(_):
        x = random() * 2 - 1
        y = random() * 2 - 1
        return 1 if x ** 2 + y ** 2 <= 1 else 0

    count = spark.sparkContext.parallelize(range(1, n + 1), 1).map(f).reduce(add)
    print("Pi is roughly %f" % (4.0 * count / n))