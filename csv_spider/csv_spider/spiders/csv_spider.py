from scrapy.spiders import CSVFeedSpider


class CsvDataset(CSVFeedSpider):
    name = 'csv_spider'
    start_urls = ['http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv']

    delimiter = ';'
    quotechar = "''"

    headers = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol', 'quality']

    def parse_row(self, response, row):
         print('pH=', row['pH'], '\tAlcohol Content =', row['alcohol'],
               '\tWine Quality =', row['quality'])