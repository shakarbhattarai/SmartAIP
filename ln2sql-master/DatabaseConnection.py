import MySQLdb
from ln2sql import ln2sql

# print all the first cell of all the rows
def get_desc(mantis):
    db = MySQLdb.connect(host="mantis.hcinsight.net",  # your host, usually localhost
                         user="i80389",  # your username
                         passwd="OhS%a3de",  # your password
                         db="mantis")  # name of the data base

    query = "select description from mantis.mantis_bug_table a, mantis.mantis_bug_text_table b where a.project_id='31' and a.id=b.id and a.id=";
    cur = db.cursor()
    cur.execute(query+"'"+mantis+"'")
    value=''
    for row in cur.fetchall():
        value=row
    db.close()
    return value

description= get_desc('49671')[0].replace('\r','')
description=description.replace('prv TIN','provider_tax_id(').replace("'","").replace('"','').replace('DOS','dos').replace('LINE_OF_BUSINESS','line_of_business').replace('!=','NOT EQUAL TO')
print description
a=ln2sql('database/hci.sql', 'lang/english.csv', 'hciflag hcilin claims'+description, 'output.json', 'thesaurus/th_english.dat',None)