import logging
class LogGeneratorClass:
    @staticmethod
    def log_generator():
        log_file=logging.FileHandler("./Logs/CredKart_automation_testing.logs")
        log_format=logging.Formatter('%(asctime)s-%(levelname)s-%(funcName)s-%(message)s')
        log_file.setFormatter(log_format)
        logger=logging.getLogger()
        logger.addHandler(log_file)
        logger.setLevel(logging.INFO)
        return logger

