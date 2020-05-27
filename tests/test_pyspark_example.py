from random import random
from unittest import TestCase
from operator import add

from pyspark.sql import SparkSession


class PySparkTest(TestCase):

    def setUp(self):
        self.spark = SparkSession \
            .builder.master('spark://spark:7077') \
            .appName("PySparkTest") \
            .getOrCreate()

    def test_pyspark_init(self):
        def f(_):
            x = random() * 2 - 1
            y = random() * 2 - 1
            return 1 if x ** 2 + y ** 2 <= 1 else 0

        partitions = 2
        n = 100000 * partitions
        count = self.spark.sparkContext.parallelize(range(1, n + 1), partitions).map(f).reduce(add)
        print("Pi is roughly %f" % (4.0 * count / n))

    def tearDown(self):
        self.spark.stop()

