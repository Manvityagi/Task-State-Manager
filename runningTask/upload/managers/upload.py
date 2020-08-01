import pandas as pd
# will have to make the table name unique
class UploadManager:
    def __init__(self,userId,file_name="Records.csv"):
        self.userId = userId
        self.file_name = file_name
        self.table_name = userId 
        self.lines = 0
        self.isPaused = False
        self.isTerminated = False
        self.progress = 0
        # super().__init__()
    
    @staticmethod
    def start(userId):
        print("in thread of manager start")
        pass #will call checkstatus here
    
    @staticmethod
    def get_checkpoint(userId):
        print("get the checkpoint")
        pass

    def pause(self):
        pass

    def resume(self):
        pass

    def check_status(self):
        pass
    
    def terminate(self):
        pass



