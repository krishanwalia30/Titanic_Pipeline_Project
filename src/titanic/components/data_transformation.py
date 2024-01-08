import os
from pathlib import Path
import pandas as pd
import numpy as np
from titanic.entity import DataTransformationConfig
# from titanic import logging
from titanic.logging import logger


from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

from titanic.utils.common import save_object


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
    
    def load_dataframe(self):
        df = pd.read_csv(os.path.join(self.config.data_path, "Titanic-Dataset.csv"))
        logger.info(f"Loaded {df.shape[0]} rows of data")
        return df
    
    def create_preprocessor(self):

        num_col = ['Age']
        cat_col = ['Sex','Embarked']

        num_pipe = Pipeline(
            steps=[
                # Handling the missing values
                ('imputing_AGE',SimpleImputer(strategy='mean')),
                # scaling 
                ('scalling_data', StandardScaler(with_mean=False)),
            ]
        )

        cat_pipe = Pipeline(
            steps=[
                # Handling the missing values
                ('imputing_AGE',SimpleImputer(strategy='most_frequent')),
                # encoding
                ('one_hot_encoder',OneHotEncoder(handle_unknown='ignore')),
                # scaling
                ('scalling_data', StandardScaler(with_mean=False)),
            ]
        )

        preprocessor = ColumnTransformer(
            [
                ('num_pipeline', num_pipe ,num_col),
                ('cat_pipeline', cat_pipe ,cat_col),
            ]
        )
        logger.info("Preprocessing pipeline")
        return preprocessor

        
        
    def initiate_pp(self):
        preprocessor_obj = self.create_preprocessor()
        df = self.load_dataframe()
        
        x = df.drop('Survived', axis = 1)
        y = df['Survived']
        
        # Train test split
        x_train,x_test,y_train,y_test = train_test_split(x,y, random_state=42, test_size=0.2)

        # Preprocessing
        x_train = preprocessor_obj.fit_transform(x_train)
        
        x_test = preprocessor_obj.transform(x_test)

        save_object(path = Path(os.path.join(self.config.root_dir,"preprocessor.pkl")),obj =preprocessor_obj)
        logger.info("Preprocessor Saved")
        
        return x_train,x_test,y_train,y_test

    
    def save_transformed_data(self):
        df = self.initiate_pp()
        