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
        self.headers = []
        self.c = connection.cursor()
        query = f"select column_name\
            from information_schema.columns\
            where table_schema = 'public' and table_name = \'{self.tableName}\';"
        data = self.c.execute(query)
        while True:
            data = self.c.fetchone()
            if data == None:
                self.headers = ','.join(self.headers)
                break
            self.headers.append(str(data[0]))
        query = f"SELECT MAX(Sid) FROM {self.tableName}"
        self.c.execute(query)
        self.total_entries = self.c.fetchone()[0]
        super().__init__()


    def start(self):
        c = connection.cursor()
        f = open(f"./{self.tableName}.csv",  'w+')
        if self.currentRow == 0:
            f = open(f"./{self.tableName}.csv",  'w')
            f.write(self.headers)
        self.isPaused = False
        self.isTerminated = False
        while(self.total_entries - self.currentRow > 0):
            try:
                self.currentRow += 1
                query = f"SELECT * FROM {self.tableName} WHERE Sid={self.currentRow}"
                data = c.execute(query)
                data = c.fetchone()
                data = ','.join(str(e) for e in data)
                f.write('\n')
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
