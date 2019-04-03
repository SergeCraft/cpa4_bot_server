import pymysql.cursors  
 
# Подключиться к базе данных.
connection = pymysql.connect(host='0.0.0.0',
							 port = 3306,
                             user='cpa4_bot_server',
                             password='forcpa4',                             
                             db='cpa4_test',
                             #charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
 
print ("connect successful!!")
 
try:  
 
    with connection.cursor() as cursor:
       
        # SQL 
        sql = "SELECT * FROM users"
         
        # Выполнить команду запроса (Execute Query).
        cursor.execute(sql)
         
        print ("cursor.description: ", cursor.description)
 
        print()
 
        for row in cursor:
            print(row)
             
finally:
    # Закрыть соединение (Close connection).      
    connection.close()