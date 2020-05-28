import sqlite3

connection = sqlite3.connect("drivers.db")

cursor = connection.cursor()

query = """ SELECT * FROM drivers """

result = cursor.execute(query)

for item in result:
	print(item)