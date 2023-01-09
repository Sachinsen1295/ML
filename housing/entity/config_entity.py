from collections import namedtuple

"""
1. Download Url 
2. Download folder (compressed file)
3. extract folder (extracted file)
4. Train datset folder
5. test dataset folder
"""

# namedtuple is immutable like tuple
# We create yaml file because we need to pass data in config folder

DataIngestionConfig = namedtuple("DataIngestionConfig",
                                 ["dataset_download_url","tgz_download_dir","raw_data_dir","ingested_train_dir","ingested_test_dir"])


DataValidationCongif = namedtuple("DataValidationCongif", ["schema_file_path"])

DataTransformationConfig = namedtuple("DataTransformationConfig", ["add_bedroom_per_room",
                                                                   "transformed_train_dir",
                                                                   "transformed_test_dir",
                                                                   "preprocessed_object_file_path"])

ModelTrainerConfig = namedtuple("ModelTrainerConfig", ["trained_model_file_path","base_accuracy"])

ModelEvaluationConfig = namedtuple("ModelEvaluationConfig",["model_evaluation_file_path","time_stamp"])

ModelPushConfig = namedtuple("ModelPushConfig",["export_dir_path"])



