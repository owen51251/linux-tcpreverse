import pyodbc
server = 'localhost\sqlexpress' 
database = 'parsar' 
username = 'sa' 
password = '1qaz@WSX' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

num=3
text="cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc"
time="2017/5/10"

SQLCommand =("INSERT INTO parser (id,con,time) VALUES (?,?,?)")
Values = [num,text,time] 
cursor.execute(SQLCommand,Values)
cnxn.commit() 
print("Data Successfully Inserted")   
cnxn.close()    