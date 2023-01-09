
from housing.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,\
    ModelTrainerConfig,ModelEvaluationConfig,ModelPushConfig,TrainingPipelineConfig
    
from housing.util.util import read_yaml_file 
# use this function read yaml file from config.yaml from util file


class Configuration:
    
    def __init__(self) -> None:
        pass
    
    def get_data_ingestion_config(self) ->DataIngestionConfig:
        pass
    
    def get_data_validation_config(Self) ->DataValidationConfig:
        pass
    
    def get_data_transformation_config(self) ->DataTransformationConfig:
        pass
    
    def get_model_trainer_config(self) ->ModelTrainerConfig:
        pass
    
    def get_model_evaluation_config(self) ->ModelEvaluationConfig:
        pass
    
    def get_model_pusher_config(self) ->ModelPushConfig:
        pass
    
    def get_training_pipeline_config(self) ->TrainingPipelineConfig:
        pass
    