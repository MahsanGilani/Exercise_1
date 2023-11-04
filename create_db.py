import psycopg2
from configparser import ConfigParser


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