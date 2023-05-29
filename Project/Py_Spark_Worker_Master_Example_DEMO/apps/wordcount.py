from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("WordCount")
sc = SparkContext(conf=conf)

# replace 'input_file.txt' with the actual path of your input file
lines = sc.textFile('/opt/spark-data/input_file.txt')
words = lines.flatMap(lambda line: line.split())
wordCounts = words.countByValue()

# replace 'output_file.txt' with the actual path of your output file
with open('/opt/spark-data/output_file.txt', 'w') as f:
    for word, count in wordCounts.items():
        f.write("{}: {}\n".format(word, count))

# print the word count results
for word, count in wordCounts.items():
    print("{}: {}".format(word, count))

sc.stop()
