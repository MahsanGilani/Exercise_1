import psycopg2
from configparser import ConfigParser

def config(filename=None,section=None):
    parser=ConfigParser()
    parser.read(filename)
    
    db_config = dict()
    if parser.has_section(section):
        params = parser.items() # list of tuples containing key and value
        for param in params:
            db_config[param[0]] = param[1]
            
    else:
        raise Exception("section {} not found".format(section))
    
    return db_config