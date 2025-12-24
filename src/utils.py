#utils will have all the common things/functionality which the entire project can use
import os
import sys
import dill # library which helps us to create pkl file


import pandas as pd
import  numpy as np
from src.exception import CustomException
def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj) 

    except Exception as e:
        raise CustomException(e,sys)     
