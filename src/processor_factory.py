from main_processor import MainProcessor

# Factory class for creating an instance of the MainProcessor
class ProcessorFactory:
    @staticmethod
    def create_processor(day_data, intraday_files):
        """
        Creates an instance of MainProcessor with the provided day data and intraday files.
        :param day_data: DataFrame containing the day data.
        :param intraday_files: List of file paths to intraday data.
        :return: An instance of MainProcessor.
        """
        return MainProcessor(day_data, intraday_files)
