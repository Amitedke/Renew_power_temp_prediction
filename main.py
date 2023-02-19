from renew.configuration.mongo_db_connection import  MongoDBClient
from renew.exception import EnergyException
import sys,os
from renew.pipeline.training_pipeline import TrainingPipeline


if __name__ == '__main__':
    training_pipeline = TrainingPipeline()
    training_pipeline.run_pipeline()
        

     
    