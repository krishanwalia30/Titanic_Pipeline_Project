import os
from sklearn.preprocessing import StandardScaler
from titanic.utils.common import load_object
from titanic.logging import logger
import pandas as pd

class PredictionPipeline:

    def __init__(self, filename):
        self.filename = filename

    
    def load_model(self):
        model = load_object(os.path.join("artifacts","model_trainer", "model.pkl"))
        return model
    

    def load_preprocessor(self):
        preprocessor = load_object(os.path.join("artifacts","data_transformation", "preprocessor.pkl"))
        return preprocessor
    

    def load_data(self):
        data = pd.read_csv(self.filename)
        return data


    def predict(self):
        # loading the model
        model = self.load_model()
        logger.info("Model has been loaded successfully for prediction")

        # loading the test data
        test_data = self.load_data()
        logger.info("Test data has been loaded successfully for prediction")
        
        # loading the preprocessor
        preprocessor = self.load_preprocessor()
        logger.info("Preprocessor has been loaded successfully for prediction")
        
        # transforming the test data
        preprocessor.transform(test_data)
        logger.info("Data has been transformed successfully for prediction")

        # predicting the test data
        predictions = model.predict(test_data)
        logger.info("Predictions has been made successfully")

        return predictions
    

        # print("=======",test_data)
        # # predicting the test data
        # predictions = model.predict(test_data)
        # logger.info("Predictions has been made successfully")

        # print(predictions)
    

        # if (predictions==1):
        #     prediction = "Survived"
        #     return [{ "image": prediction}]
        # else:
        #     prediction = "Coccidiosis"
        #     return [{ "image": prediction}]
    
    # def transform_data(self):
    #     # loading the data
    #     test_data = pd.read_csv(self.filename)
    #     # logger.info("Test data has been loaded successfully")

    #     # print(">>>>>>>>>>", test_data)

    #     test_data["Sex"] = test_data["Sex"].map({"Male": 0, "Female": 1})
    #     # print(">>>>>>>>>>", test_data)
        
    #     # test_data = test_data.dropna(subset=["Embarked"])

    #     # test_data['Age'] = test_data['Age'].fillna(value=int(test_data['Age'].mean()))

    #     test_data["Embarked"] = test_data["Embarked"].map({"S": 0, "C": 1, "Q": 2})

    #     # scaling the dataset
    #     # sdscaler = StandardScaler()
    #     # test_data= sdscaler.fit_transform(test_data)
    #     print(">>>>>>>>>>", test_data)

    #     return test_data
