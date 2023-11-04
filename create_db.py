import psycopg2
from configparser import ConfigParser
# from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def config(filename=None,section=None):
    parser=ConfigParser()
    parser.read(filename)
    
    db_config = dict()
    if parser.has_section(section):
        params = parser.items(section) # list of tuples containing key and value for that section
        for param in params:
            db_config[param[0]] = param[1]
            
    else:
        raise Exception("section {} not found".format(section))
    
    return db_config

def connect (conn, cur): # cursor execute the query
    # if someone was connecting to the database and the connection was established
    if conn and cur:
        conn , cur , local_connection = conn, cur, False  # conn and cur are the same
        # when local_connection is false, means that the connection was established before, and was not established here
    else:
        try:
            params = config(filename='database.ini', section='xxxx') # the result is dictionary
            print(params)
            conn = psycopg2.connect (**params)
            cur = conn.cursor()
            local_connection = True
            
        except (Exception, psycopg2.DatabaseError) as e:
            print(e)
            conn , cur, local_connection = None, None, None
            
    return conn, cur, local_connection

connect(conn=None , cur=None)


#creating tables: # its a good idea to have classes and define our methods there.

# def create_table():
#     conn , cur, local_connection = connect(conn=None , cur=None)
#     # istead of line 47, we can also use the below code for our connection to be autocommit
#     # conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
#     query = """CREATE TABLE IF NOT EXISTS ticket(ticket_id SERIAL PRIMARY KEY, credit INTEGER, expire_date TIMESTAMP)"""
#     cur.execute(query)
#     conn.commit() # if we dont commit, the table will not be created, because postgres is on readingcommit isolation level

# def create_table():
#     conn , cur, local_connection = connect(conn=None , cur=None)
#     query = """CREATE TABLE IF NOT EXISTS user_ticket(
#         user_ticket_id SERIAL PRIMARY KEY,
#         user_id INTEGER REFERENCES travel_user(user_id),
#         ticket_id INTEGER REFERENCES ticket(ticket_id)
#     );"""
#     cur.execute(query)
#     conn.commit()

# def create_table():
#     conn , cur, local_connection = connect(conn=None , cur=None)
#     query = """CREATE TABLE IF NOT EXISTS user_travel(
#         user_travel_id SERIAL PRIMARY KEY,
#         user_id INTEGER REFERENCES travel_user(user_id),
#         travel_id INTEGER REFERENCES travel(travel_id)
#     );"""
#     cur.execute(query)
#     conn.commit()
    
# def create_table():
#     conn , cur, local_connection = connect(conn=None , cur=None)
#     query = """CREATE TABLE IF NOT EXISTS bank(
#         bank_id SERIAL PRIMARY KEY,
#         balance INTEGER,
#         user_id INTEGER REFERENCES travel_user(user_id)
#     );"""
#     cur.execute(query)
#     conn.commit()
    
# create_table()