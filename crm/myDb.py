import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'ad257'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE crm")

print("all done")