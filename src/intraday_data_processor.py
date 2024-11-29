import pandas as pd

# Class to process intraday data for volume and calculate crossover times
class IntradayVolumeProcessor:
    def process_intraday_data(self, intraday_data, stock_averages):
        """
        Processes intraday data and calculates the crossover time for stock volume.
        :param intraday_data: DataFrame containing intraday stock data.
        :param stock_averages: Dictionary containing 30-day average volume for each stock.
        :return: List of dictionaries with stock name, date, and crossover time.
        """
        results = []
        
        # Combine 'Date' and 'Time' into a 'Datetime' column
        intraday_data['Datetime'] = pd.to_datetime(intraday_data['Date'].astype(str) + ' ' + intraday_data['Time'], dayfirst=True)
        
        # Filter data to only include trades after market open at 09:15
        intraday_data = intraday_data[intraday_data['Time'] >= "09:15:00"]

        # Loop through each stock to calculate the cumulative volume and find crossover times
        for stock in intraday_data['Stock Name'].unique():
            stock_data = intraday_data[intraday_data['Stock Name'] == stock].copy()
            stock_data.set_index('Datetime', inplace=True)
            
            # Calculate the cumulative volume over the last 60 minutes
            stock_data['Cumulative Volume'] = stock_data['Last Traded Quantity'].rolling('60min').sum()
            
            # Find the first time the cumulative volume exceeds the average stock volume
            crossover_time = stock_data[stock_data['Cumulative Volume'] > stock_averages.get(stock)].index.min()
            
            # If a crossover time exists, add it to the results list
            if crossover_time:
                results.append({'Date': stock_data.index.date[0], 'Stock Name': stock, 'Crossover Time': crossover_time.time()})
        
        return results
