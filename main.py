# main.py
import sys
import logging
from src.exception import CustomException

if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(e, sys)
