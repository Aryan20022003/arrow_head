import pandas as pd

# Class to handle the loading of stock data from a CSV file
class StockDataProcessor:
    def __init__(self, file_path):
        """
        Initializes the StockDataProcessor with the path to the stock data CSV file.
        :param file_path: Path to the CSV file containing stock data.
        """
        self.file_path = file_path

    def load_data(self):
        """
        Loads the stock data from the CSV file and parses the 'Date' column as datetime.
        Returns a pandas DataFrame containing the stock data.
        :return: pandas DataFrame containing the stock data.
        """
        try:
            return pd.read_csv(self.file_path, parse_dates=['Date'], dayfirst=True)
        except Exception as e:
            print(f"Error loading data: {e}")
            return None
