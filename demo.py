import sys
from random import random
from operator import add

from pyspark.sql import SparkSession


if __name__ == "__main__":
    """
        Usage: pi [partitions]Initial job has not accepted any resources; check your cluster UI to ensure that worke
    """
    spark = SparkSession\
        .builder.master('spark://spark:7077')\
        .config('spark.executor.memory', '471859200')\
        .config('spark.driver.cores', '1')\
        .appName("PythonPi")\
        .getOrCreate()

    partitions = 1
    n = 1 * partitions

    def f(_):
        x = random() * 2 - 1
        y = random() * 2 - 1
        return 1 if x ** 2 + y ** 2 <= 1 else 0

    count = spark.sparkContext.parallelize(range(1, n + 1), 1).map(f).reduce(add)
    print("Pi is roughly %f" % (4.0 * count / n))

    spark.stop()