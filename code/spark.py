from pyspark.sql import SparkSession

class spark ():
    
    def __init__(self, MONGODB_ATLAS_URI) -> None:
        spark = SparkSession. \
            builder. \
            appName("pyspark-notebook"). \
            master("spark://spark-master:7077"). \
            config("spark.executor.memory", "2g"). \
            config("spark.mongodb.input.uri", MONGODB_ATLAS_URI). \
            config("spark.mongodb.output.uri", MONGODB_ATLAS_URI). \
            config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.12:3.0.1,org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.0"). \
            getOrCreate()
        pass

class kafka ():

    def load_df_from_kafka(spark_s, topic):
        return spark_s \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "broker:29092") \
        .option("subscribe", topic) \
        .load()