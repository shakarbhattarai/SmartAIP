import pyodbc
import MySQLdb
import pandas.io.sql as psql

# print all the first cell of all the rows
def get_desc(mantis):
    connection_info = MySQLdb.connect(host="192.168.72.30:1521",  # your host, usually localhost
                         user="scott",  # your username
                         passwd="oracle",  # your password
                         db="orcl")  # name of the data base

    query = "select description from mantis.mantis_bug_table a, mantis.mantis_bug_text_table b where a.project_id='31' and a.id=b.id and a.id=";
    cur = connection_info.cursor()


    cnxn = pyodbc.connect(connection_info)
    cursor = cnxn.cursor()
    sql = "SELECT * FROM TABLE"

    df = psql.frame_query(sql, cnxn)
    cnxn.close()

