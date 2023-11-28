import os 
import sys
import logging


logging_str="[%(asctime)s : %(levelname)s : %(module)s]: %(message)s"

log_dir="logs"

log_dir_path =  

log_filepath=os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    #filename=log_filepath,
    level=logging.INFO, #level of the message
    format=logging_str  #format of the message
    handlers=[
        logging.FileHandler(log_filepath),  #file handler
        logging.StreamHandler(sys.stdout)   #stream handler
    ]

logger=logging.getLogger("CNNClassifier")
