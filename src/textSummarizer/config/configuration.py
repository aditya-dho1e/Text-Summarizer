from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories

from textSummarizer.entity import (DataIngestionConfig)

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = Path('config/config.yaml'),
        params_filepath = Path('params.yaml')):

        self.config = read_yaml(config_filepath) # creates the artifacts folder
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    
    # DataIngestionConfig is the return type of the below funtion (which we created earlier)
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        # this is the return type of the function
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config