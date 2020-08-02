import pandas as pd
from django.db import connection
from download.managers.exception import InterruptException


class DownloadManager:
    def __init__(self, userId):
        self.userId = userId
        self.tableName = userId
        self.currentRow = 0
        self.isPaused = False
        self.isTerminated = False
        self.progress = 0
        self.headers = ""
        query = f"SELECT MAX(Sid) FROM {self.tableName}"
        self.total_entries = c.execute(query)
        super().__init__()


    def start(self):
        c = connection.cursor()
        f = open(f"./{self.tableName}.csv",  'w+')
        self.isPaused = False
        self.isTerminated = False
        while(self.total_entries - self.currentRow > 0):
            try:
                self.currentRow += 1
                query = f"SELECT * FROM {self.tableName} WHERE SNo={self.currentRow}"
                data = c.execute(query)
                f.write(data)
            except InterruptException:
                f.close()
                return


    def pause(self):
        self.isPaused = True

    def resume(self):
        self.start()

    def check_status(self):
        return self.isPaused or self.isTerminated

    def terminate(self):
        """
            Rollback
        """
        c = connection.cursor() 
        self.isTerminated = True
        query = f"DROP TABLE IF EXISTS {self.tableName}"
        c.execute(query)        
