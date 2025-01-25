import os
import sys
from src.exception import CustomException  
from src.logger import logging 

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass 

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

# In the class below we want to give input (like where to save train/test/raw data etc.)
# Decorator @dataclass will help us directly define the class variable, otherwise inside
# a class we use __init__ to define a variable... with @dataclass we don't need __init__

# We are first making the DataIngestionConfig to take our input data and store them as .csv files in artifacts folder
# If we are just going to use a class for DEFINING VARIABLES, then we can use these decorators....if we are having functions within classes, use __init__() itself

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv") #create a aritifats folder and stroing the train data in it
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() #You create a DataIngestion object and it automatically creates its own DataIngestionConfig object. As a result, all 3 paths defined above will get saved in ingestion_config class variable

    def intiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # Can also read from MongoDB, APIs and other DBs
            df=pd.read_csv(r'notebook\data\StudentsPerformance.csv')  # Using raw string
            logging.info('Read the dataset as dataframe')

            # We have created the path directions above in DataIngestionConfig(). below we give the command to create the folders ('artifacts') and save the data in them
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            
            logging.info("Train test split initiated")

            # Splitting the data into train and test sets
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Saving the train and test sets
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )

        except Exception as e:
            raise CustomException(e, sys)

'''
index=False: This argument indicates that you do not want to write row indices to the CSV file. 
'''

'''
if __name__ == "__main__":
    data_ingestion = DataIngestion()
    data_ingestion.intiate_data_ingestion()

    '''