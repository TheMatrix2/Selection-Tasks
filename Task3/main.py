from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import col, collect_list, lit


def get_pairs(df):
    product_categories = df.groupBy("Product").agg(collect_list("Category").alias("Categories"))
    product_category_pairs = product_categories.select(
        col("Product"),
        col("Categories"),
    ).withColumn("Category", col("Categories")).explode("Category")
    without_categories = df.select("Product").distinct().subtract(product_category_pairs.select("Product"))
    without_categories = without_categories.withColumn("Category", lit(None))

    result = product_category_pairs.union(without_categories)

    return result


if __name__ == "__main__":
    spark = SparkSession.builder.appName("ProductCategory").getOrCreate()

    data = [("Product1", "Category1"),
            ("Product1", "Category2"),
            ("Product2", "Category1"),
            ("Product3", "Category3")]

    dataframe = spark.createDataFrame(data, ["Product", "Category"])

    res = get_pairs(dataframe)

    res.show()

    spark.stop()
