from titanic.components.data_transformation import DataTransformation
from titanic.config.configuration import ConfigurationManager

class DataTransformationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_tranformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(data_tranformation_config)
        data_transformation.save_transformed_data()