import pandas as pd
from intraday_data_processor import IntradayVolumeProcessor  # Ensure this import is added

# Main processor class to handle calculating 30-day averages and processing data
class MainProcessor:
    def __init__(self, day_data, intraday_files):
        """
        Initializes the MainProcessor with the day data and a list of intraday files.
        :param day_data: DataFrame containing day data (stock data over time).
        :param intraday_files: List of file paths for intraday stock data.
        """
        self.day_data = day_data
        self.intraday_files = intraday_files

    def calculate_30_day_average(self, intraday_dates):
        """
        Calculates the 30-day average volume for each stock on given dates.
        :param intraday_dates: List of dates for which to calculate the 30-day average.
        :return: Dictionary with stock names as keys and their 30-day average volumes as values.
        """
        averages = {}
        for intraday_date in intraday_dates:
            # Filter the day data for the past 30 days relative to the intraday date
            relevant_days = self.day_data[
                (self.day_data['Date'].dt.date < intraday_date) & 
                (self.day_data['Date'].dt.date >= (pd.to_datetime(intraday_date) - pd.Timedelta(days=30)).date())
            ]
            
            # Calculate the average volume per stock over the last 30 days
            avg_volume = relevant_days.groupby('Stock Name')['Volume'].mean()
            averages[intraday_date] = avg_volume.to_dict()
        
        return averages

    def process_data(self):
        """
        Processes the intraday data files and calculates crossover times based on stock volume.
        :return: List of dictionaries with results containing stock name, date, and crossover time.
        """
        all_results = []
        
        # Loop through each intraday file and process it
        for intraday_file in self.intraday_files:
            try:
               
                intraday_data = pd.read_csv(intraday_file)
              
                intraday_data['Date'] = pd.to_datetime(intraday_data['Date'], dayfirst=True).dt.date
                intraday_date = intraday_data['Date'].iloc[0]

     
                stock_averages = self.calculate_30_day_average([intraday_date])[intraday_date]
                
          
                intraday_processor = IntradayVolumeProcessor()
                intraday_results = intraday_processor.process_intraday_data(intraday_data, stock_averages)
                
                all_results.extend(intraday_results)
            except Exception as e:
                print(f"Error processing intraday file {intraday_file}: {e}")
        
        return all_results
