import sqlite3
connection = sqlite3.connect("beauty_salon.db")
cursor = connection.cursor()
sql_command = """CREATE TABLE IF NOT EXISTS employee (
ID INTEGER PRIMARY KEY,
JMBG INTEGER ,
first_name VARCHAR(30),
last_name VARCHAR(30),
date_of_birth DATE,
date_of_employment DATE,
work_position VARCHAR(100));"""
cursor.execute(sql_command)
connection.close()

connection = sqlite3.connect("beauty_salon.db")
cursor = connection.cursor()
sql_command = """CREATE TABLE IF NOT EXISTS client (
ID INTEGER PRIMARY KEY,
JMBG INTEGER ,
first_name VARCHAR(30),
last_name VARCHAR(30),
date_of_birth DATE)"""
cursor.execute(sql_command)
connection.close()


