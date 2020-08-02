import pandas as pd
from django.db import connection
from upload.managers.exception import InterruptException


class UploadManager:
    def __init__(self, userId, file_name="Records.csv"):
        self.userId = userId
        self.file_name = file_name
        self.table_name = userId
        self.lines_read = 0
        self.isPaused = False
        self.isTerminated = False
        self.progress = 0
        self.headers = ""
        super().__init__()

    def create_table(self):
        try:
            c = connection.cursor()
            query = f'CREATE TABLE {self.table_name} (\
            Sid SERIAL PRIMARY KEY, \
            Region varchar(255), \
            Country varchar(255), \
            "Item Type" varchar(255), \
            "Sales Channel" varchar(255), \
            "Order Priority" varchar(255), \
            "Order ID" varchar(255), \
            "Units Sold" FLOAT,\
            "Unit Price" FLOAT,\
            "Unit Cost" FLOAT,\
            "Total Revenue" FLOAT,\
            "Total Cost" FLOAT,\
            "Total Profit" FLOAT\
            );'
            c.execute(query)
            df = pd.read_csv(self.file_name, skiprows=self.lines_read)
            rows_list = [list(row) for row in df.values]
            self.headers = df.columns.to_list()
            tmp = ""
            for i in self.headers:
                if(len(tmp) != 0):
                    tmp += ","
                if len(str(i).split(' ')) == 1:
                    tmp += str(i)
                else:
                    tmp += "\"" + str(i) + "\""
            self.headers = tmp
        finally:
            c.close()

    def start(self):
        c = connection.cursor() 
        if(self.lines_read == 0):
            self.create_table()
        self.isPaused = False
        self.isTerminated = False
        df = pd.read_csv(self.file_name, skiprows=self.lines_read)
        rows_list = [list(row) for row in df.values]
        for row in rows_list:
            try:
                tmp = ""
                for i in row:
                    if(len(tmp) != 0):
                        tmp += ","
                    tmp += "\'" + str(i) + "\'"
                row = tmp
                query = f"INSERT INTO {self.table_name}({self.headers}) VALUES({row});"
                # print(query)
                c.execute(query)
                self.lines_read += 1
                status = self.check_status()
                print(status)
                if(status):
                    raise InterruptException
            except InterruptException:
                break

    # def get_checkpoint(self):
    #     query = f"SELECT MAX(Sid) from {self.table_name}"
    #     roll_back_checkpoint = self.c.execute(query)
    #     return roll_back_checkpoint

    def pause(self):
        self.isPaused = True

    def resume(self):
        self.isPaused = False
        self.start()

    def check_status(self):
        return self.isPaused or self.isTerminated

    def terminate(self):
        """
            Rollback
        """
        c = connection.cursor() 
        self.isTerminated = True
        query = f"DROP TABLE IF EXISTS {self.table_name}"
        c.execute(query)        
