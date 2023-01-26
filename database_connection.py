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

connection = sqlite3.connect("beauty_salon.db")
cursor = connection.cursor()
sql_command = """CREATE TABLE IF NOT EXISTS services (
ID INTEGER PRIMARY KEY,
nail_extension VARCHAR(30) ,
nail_correction VARCHAR(30),
permanent_varnish VARCHAR(30),
make_up VARCHAR(30),
waxing VARCHAR(30))"""
cursor.execute(sql_command)
connection.close()

connection = sqlite3.connect("beauty_salon.db")
cursor = connection.cursor()
sql_command = """CREATE TABLE IF NOT EXISTS price_list (
ID INTEGER PRIMARY KEY,
nail_extension VARCHAR(30) ,
nail_correction VARCHAR(30),
permanent_varnish VARCHAR(30),
make_up VARCHAR(30),
waxing VARCHAR(30))"""
cursor.execute(sql_command)
connection.close()


