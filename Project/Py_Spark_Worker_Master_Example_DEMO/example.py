from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("example") \
    .master("spark://localhost:9090") \
    .getOrCreate()

# create an RDD
rdd = spark.sparkContext.parallelize(range(1000))

# perform operations on the RDD
rdd_filtered = rdd.filter(lambda x: x % 2 == 0)
sum_of_evens = rdd_filtered.reduce(lambda a, b: a + b)

# print the result
print("Sum of even numbers:", sum_of_evens)

# stop the SparkSession
spark.stop()
