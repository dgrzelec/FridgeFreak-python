# import databases
# import sqlalchemy
from fridgefreak_api.config import config
from mysql.connector import connect, MySQLConnection



# metadata = sqlalchemy.MetaData()

# engine = sqlalchemy.create_engine(config.DATABASE_URL,
#                                     connect_args={"check_same_thread": False}) #for sqlite only

# table_definition = sqlalchemy.text("CREATE TABLE IF NOT EXISTS `products` (\
#                                     `id` int NOT NULL,\
#                                     `name` text,\
#                                     `quantity` int DEFAULT NULL,\
#                                     `category` text,\
#                                     `storage_space` text,\
#                                     `expire_by` date DEFAULT NULL,\
#                                     PRIMARY KEY (`id`)\
#                                     );")

# with engine.begin() as conn:
#     conn.execute(table_definition)



def get_mysql_connector():
    return  connect()(
        host=config.DATABASE_HOST,
        user=config.DATABASE_USER,
        password=config.DATABASE_PASSWORD,
        database=config.DATABASE_NAME
        )

####

connection = MySQLConnection(
        host=config.DATABASE_HOST,
        user=config.DATABASE_USER,
        password=config.DATABASE_PASSWORD,
        database=config.DATABASE_NAME
        )


if __name__ == "__main__":
    # mydb =  get_mysql_connector()
    
    connection.connect()
    
    # print table info
    mycursor = connection.cursor()

    mycursor.execute("SHOW CREATE TABLE products;")

    myresult = mycursor.fetchall()

    print(myresult[0][1].format())

    connection.close()