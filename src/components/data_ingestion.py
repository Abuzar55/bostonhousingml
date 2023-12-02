
import sys
import os
import pandas as pd
from src.logger import logging
from src.exceptions import CustomException
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# Now there is a need to make 2 classes. In the modular programming we need to save data as training and testing and this is the code for that
@dataclass
class DataIngesConfig:
    train_data_path = os.path.join('artifacts', 'train_data.csv')
    test_data_path = os.path.join('artifacts', 'test_data.csv')
    raw_data_path = os.path.join('artifacts', 'raw_data.csv')

class DataIngestion:
    def __init__(self):
        logging.info('Entered the data ingestion class')
        self.data_inges_config = DataIngesConfig()
    
    def initiate_data_ingestion(self):
        try:
            # Read the raw data from csv file and store it in a dataframe, it can be from any source such as SQL, mongo DB, API
            logging.info('initialted data ingestion--reading data')
            df = pd.read_csv('notebook\data\stud.csv')
            os.makedirs(os.path.dirname(self.data_inges_config.raw_data_path), exist_ok=True)
            df.to_csv(self.data_inges_config.raw_data_path, index=False, header=True)

            logging.info('entering train test split')
            train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)
            os.makedirs(os.path.dirname(self.data_inges_config.train_data_path), exist_ok=True)
            os.makedirs(os.path.dirname(self.data_inges_config.test_data_path), exist_ok=True)
            train_data.to_csv(self.data_inges_config.train_data_path, index = False, header = True)
            train_data.to_csv(self.data_inges_config.test_data_path, index = False, header = True)
            logging.info('train test split completed')
            return self.data_inges_config.raw_data_path, self.data_inges_config.train_data_path, self.data_inges_config.test_data_path
    
        except Exception as e:
            raise CustomException(e, sys)

if __name__ =="__main__":
    OBJ = DataIngestion()
    OBJ.initiate_data_ingestion()