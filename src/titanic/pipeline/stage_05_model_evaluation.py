from titanic.components.model_evaluation import ModelEvaluation
from titanic.config.configuration import ConfigurationManager

class ModelEvaluationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(model_evaluation_config)
        model_evaluation.save_metrics()
