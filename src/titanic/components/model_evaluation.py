from titanic.entity import ModelEvaluationConfig
from titanic.utils.common import load_object
from sklearn.metrics import accuracy_score, confusion_matrix
from titanic.logging import logger
import pandas as pd
import yaml

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config


    def fetch_dataset(self):
        df = pd.read_csv(self.config.data_path)
        logger.info("Data loaded successfully for model evaluation")
        return df
    

    def fetch_preprocessor(self):
        preprocessor = load_object(self.config.preprocessor_path)
        logger.info("Preprocessor loaded successfully for model evaluation")
        return preprocessor
    
    
    def fetch_model(self):
        model = load_object(self.config.model_path)
        logger.info("Model loaded successfully for model evaluation")
        return model
    

    def initiate_model_evaluation(self):
        preprocessor = self.fetch_preprocessor()
        model = self.fetch_model()
        data = self.fetch_dataset()

        x = data.drop(columns=['Survived'], axis=1)
        y = data['Survived']

        # Preprocessing the dataset
        x = preprocessor.transform(x)
        logger.info("Preprocessing done successfully for model evaluation")

        # Model Prediction
        y_pred = model.predict(x)
        logger.info("Model evaluation done successfully for model evaluation")

        # Evaluation of model
        accuracy = accuracy_score(y, y_pred)
        logger.info("Accuracy of model evaluation: {}".format(accuracy))

        accuracy = accuracy_score(y_true=y, y_pred=y_pred)
        cm = confusion_matrix(y_true=y, y_pred=y_pred)

        content = dict()
        content['accuracy'] = str(accuracy)
        content['confusion_matrix'] = str(cm)

        return content

    
    def save_metrics(self):
        content = self.initiate_model_evaluation()
        logger.info(f"Metrics saved to {self.config.metrics_file_name}")

        with open(self.config.metrics_file_name, 'w') as f:
            yaml.dump(content, f)