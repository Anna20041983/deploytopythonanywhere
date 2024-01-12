import mysql.connector
import dbconfig as cfg

class DataDAO:
    connection = ""
    cursor = ""
    host = ""
    user = ""
    password = ""
    database = ""

    def __init__(self):
        self.host = cfg.mysql['host']
        self.user = cfg.mysql['user']
        self.password = cfg.mysql['password']
        self.database = cfg.mysql['database']

    def getcursor(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()

    def create(self, values):
        cursor = self.getcursor()
        sql = "INSERT INTO data (year, sex, age_group, average_height) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, values)
        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid

    def getAll(self):
        cursor = self.getcursor()
        sql="select * from data"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            returnArray.append(self.convertToDictionary(result))
        
        self.closeAll()
        return returnArray

    def findByYear(self, year):
        cursor = self.getcursor()
        sql="select * from data where year = %s"
        values = (year,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    def update(self, values):
        cursor = self.getcursor()
        sql="update data set sex=%s, age_group= %s, average_height=%s  where year = %s"
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        print("update done")

    def delete(self, year):
        try:
            cursor = self.getcursor()
            sql = "DELETE FROM data WHERE year = %s"
            values = (year,)
            cursor.execute(sql, values)
            self.connection.commit()
            self.closeAll()
            print("Delete done")
        except Exception as e:
            print("Error deleting data:", e)
    
    def convertToDictionary(self, result):
        colnames = ['year', 'sex', 'age_group', 'average_height']
        item = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value

        return item

# Create an instance of the DataDAO class
dataDAO = DataDAO()

