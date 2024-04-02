from pyspark.sql import SparkSession


def get_pairs(df):
    print('Dataframe')
    df.show()
    print('Product(s) without category')
    df.select('Product').filter("Category like '' ").show()
    print('Pairs "Product" - "Category"')
    df.sort('Product').filter('Category != "" and Product != "" ').show()


if __name__ == "__main__":
    spark = SparkSession.builder.appName("ProductCategory").getOrCreate()

    data = [("Product1", "Category1"),
            ("Product1", "Category2"),
            ("", "Category4"),
            ("Product2", "Category1"),
            ("Product3", "Category3"),
            ("Product4", ""),]

    dataframe = spark.createDataFrame(data, ["Product", "Category"])

    get_pairs(dataframe)

    spark.stop()
