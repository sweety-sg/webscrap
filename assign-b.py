import mysql.connector
from mysql.connector import Error


# def connect():
#     """ Connect to MySQL database """
#     conn = None
#     try:
#         conn = mysql.connector.connect(
#                 host ="127.0.0.1" , 
#                 user = "root" , 
#                 passwd="Mmsp13061402@",
#                 database = "img" ,
#                 auth_plugin = "caching_sha2_password" ,
#                 port = 3306
#                 )
#         if conn.is_connected():
#             print('Connected to MySQL database')

#     except Error as e:
#         print(e)

#     finally:
#         if conn is not None and conn.is_connected():
#             conn.close()


# if __name__ == '__main__':
#     connect()
# import mysql.connector

mydb  = mysql.connector.connect(
    host ="127.0.0.1" , 
    user = "root" , 
    passwd="Mmsp13061402",
    database = "img" ,
    auth_plugin = "caching_sha2_password" ,
    port = 3306
    )


mycursor = mydb.cursor()



usname = input("Enter username: ")

def check_uname(func):
    def inner(uname):
        mycursor.execute("select * from user where username= %s", (usname,))
        result = mycursor.fetchone() 
        if result is not None :
                return func(uname)
        # for i in mycursor:
        #     print(i)
        # print(mycursor)
        # print(uname)
        raise Exception("Sorry username doesn't exist")
        
    return inner  

@check_uname
def mainfunc(uname) :
    print("function executed for username: " + uname)      
                 
mainfunc = check_uname(mainfunc)
mainfunc(usname)
mydb.close()
    

# def check(username) :

# def with_conn(f):
#     def with_connection_(*args, **kwargs):
#         conn = mysql.connector.connect(host ="121.0.0.1" , port = "3000")
#         try:
#             result = f(*args, connection=conn, **kwargs)
#         except:
#             conn.rollback()
#             print("SQL failed")
#             raise
#         else:
#             conn.commit()
#         finally:
#             conn.close()
#         return result
#     return with_connection_

# @with_conn
# def GetUsername(*args, **kwargs):
#     conn = kwargs.pop("connection")
#     Cursor = conn.cursor()
#     query = "select username from users where username = %s"
#     Cursor.execute(query, (args[0],))
#     result = Cursor.fetchone()
#     return result