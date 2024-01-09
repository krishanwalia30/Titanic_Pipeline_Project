import os
from pathlib import Path
from sklearn.metrics import accuracy_score
from titanic.entity import ModelTrainerConfig
from titanic.logging import logger
from sklearn.neighbors import KNeighborsClassifier
from titanic.utils.common import load_object, save_object
from titanic.config.configuration import ConfigurationManager as ConfMan
from titanic.components.data_transformation import DataTransformation 

from sklearn.metrics import accuracy_score

class ModelTrainer:
    def __init__(self, config:ModelTrainerConfig):
        self.config = config

    def fetch_preprocessor(self, preprocessor_file_path):
        preprocessor_obj = load_object(Path(preprocessor_file_path))
        return preprocessor_obj
    
    def initiate_model_training(self):
        config = ConfMan()
        data_tranformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(data_tranformation_config)
        train_data, test_data, preprocessor_file_path = data_transformation.initiate_data_transformation()
        x_train, y_train, x_test, y_test = (
                train_data[:,:-1],
                train_data[:,-1],
                test_data[:,:-1],
                test_data[:,-1]
        )

        model = KNeighborsClassifier(n_neighbors=30,p=1, leaf_size=75) # 0.7877094972067039
        # model = AdaBoostClassifier() # 0.7821229050279329
        # model = CatBoostClassifier(learning_rate=0.0005, iterations=2000) # 0.7877094972067039

        model.fit(x_train, y_train)

        y_pred = model.predict(x_test)

        accuracy_of_model = accuracy_score(y_test, y_pred)
        logger.info(f"The accuracy of the model is: {accuracy_of_model}")

        model_path= Path(os.path.join(self.config.root_dir,"model.pkl"))

        save_object(path = model_path,obj =model)
        logger.info(f"Model has been saved to: {model_path} with accuracy: {accuracy_of_model}")