import pandas as pd
from stock_data_processor import StockDataProcessor
from processor_factory import ProcessorFactory
from intraday_data_processor import IntradayVolumeProcessor

def main():
    day_data_file = "data/SampleDayData.csv"
    intraday_files = ["data/19thAprilSampleData.csv", "data/22ndAprilSampleData.csv"]

    stock_data_processor = StockDataProcessor(day_data_file)
    day_data = stock_data_processor.load_data()

    if day_data is not None:
        processor = ProcessorFactory.create_processor(day_data, intraday_files)
        
        all_results = processor.process_data()

        try:
            results_df = pd.DataFrame(all_results)
            results_df.to_csv('result/crossover_times.csv', index=False)
            print("Results saved to crossover_times.csv")
        except Exception as e:
            print(f"Error saving results: {e}")
    else:
        print("Failed to load day data.")

if __name__ == "__main__":
    main()
