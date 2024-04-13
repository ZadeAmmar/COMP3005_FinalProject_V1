from defs import *
import getData
import psycopg

def renewAllTables():
    tableNames = allSets.keys()
    with psycopg.connect("dbname=3005fp user=postgres password=1234") as db:
        with db.cursor() as cursor:
            for table in tableNames:
                cursor.execute(f"DROP TABLE IF EXISTS {table} CASCADE")
            
            with open('./tables.sql', 'r') as file:
                cursor.execute(file.read())
        db.commit()

def importAllTables():
    tableNames = allSets.keys()
    with psycopg.connect("dbname=3005fp user=postgres password=1234") as db:
        with db.cursor() as cursor:
            for table in tableNames:
                with open(f"../collective_data/{table}.csv", 'r', encoding='utf-8') as f:
                    header = f.readline()
                with cursor.copy(f"COPY {table} ({header}) FROM STDIN WITH CSV HEADER") as cp:
                    with open(f"../collective_data/{table}.csv", 'r', encoding='utf-8') as f:
                        data = f.read()
                    cp.write(data)

        
       
def main():
    renewAllTables()
    importAllTables()

main()