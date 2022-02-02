import csv
import pymysql
import time
from webbrowser import Error
from multiprocessing import Process

def clear_db():
    try:
        connection = pymysql.connect(host='localhost',user='groot',password='groot',db='primary_base', autocommit=True)
        cursor=connection.cursor()
        cursor.execute('TRUNCATE TABLE primary_sheet')
        cursor.execute('TRUNCATE TABLE secondary_sheet')
    except Error as e:
        print(e)
    finally:
        connection.close()

def insert_db(table_name, data):
    try:
        connection = pymysql.connect(host='localhost',user='groot',password='groot',db='primary_base', autocommit=True)
        cursor=connection.cursor()
        sql = 'INSERT INTO ' + table_name + ' (id, name) VALUES (%s, %s)'
        cursor.executemany(sql, data)
    except Error as e:
        print(e)
    finally:
        connection.close()

def get_db():
    try:
        connection = pymysql.connect(host='localhost',user='groot',password='groot',db='primary_base')
        cursor = connection.cursor()
        sql = 'SELECT p.id, p.name FROM secondary_sheet as s INNER JOIN primary_sheet as p ON s.id = p.id  WHERE p.name <> s.name'
        cursor.execute(sql)
        return cursor
    except Error as e:
        print(e)
    finally:
        connection.close()

def format_name(name):
    switch = {
    }
    name = switch.get(name)
    return name

def read_csv(filename, delimiter):
    with open(filename) as csvfile:
        data = list(csv.reader(csvfile, delimiter=delimiter))
    return data

def init(file_name, delimiter, table_name):
    csv_data = read_csv(file_name, delimiter)
    line_count = 0
    data = []
    for row in csv_data:
        if line_count == 0:
            line_count += 1
        else:
            id = row[0]
            name_value = row[1]
            name = format_name(name_value)
            if id != '0':
                data.append([id, name])
            line_count += 1
            line_count += 1
    insert_db(table_name, data)

def write_csv():
    data = get_db()
    with open('new_data.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in data.description])
        csv_writer.writerows(data)

if __name__ == '__main__':
    primary_sheet_file = 'data.txt'
    primary_sheet_table = 'primary_sheet'
    primary_sheet_delimiter = '\t'
    secondary_sheet_file = 'data2.txt'
    secondary_sheet_table = 'secondary_sheet'
    secondary_sheet_delimiter = ';'

    print('starting process ' + time.ctime())

    opt = input('clear tables? (y/n)')
    if opt == 'y':
        clear_db()

    threads = [
        Process(target = init, args=(primary_sheet_file, primary_sheet_delimiter, primary_sheet_table,)),
        Process(target = init, args=(secondary_sheet_file, secondary_sheet_delimiter, secondary_sheet_table,))
    ]
    for thread in threads:
        thread.start()

    eli_count = 0
    while thread.is_alive():
        print('loading', '.'*(eli_count+1), ' '*(2-eli_count), end='\r')
        eli_count = (eli_count + 1) % 10
        time.sleep(0.2)

    for thread in threads:
        thread.join()

    print('exporting data')
    write_csv()

    print('done      ' + time.ctime())
