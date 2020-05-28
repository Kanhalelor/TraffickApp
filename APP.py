import sqlite3
from tkinter import *

root = Tk()
root.title("Traffic App")

def exit_gui():
	return root.destroy()

def submit_data():
	"""Function to handle sqlite commands"""
	db = sqlite3.connect("drivers.db")

	# create a cursor
	cursor = db.cursor()

	# create table
	create_table = """ CREATE TABLE IF NOT EXISTS drivers (
		name TEXT NOT NULL,
		gender TEXT NOT NULL,
		speed INTEGER NOT NULL
		)"""
	cursor.execute(create_table)

	cursor.execute(" INSERT INTO drivers VALUES (:NAME_ENTRY, :GENDER_ENTRY, :SPEED_ENTRY)",
			{
				'NAME_ENTRY': NAME_ENTRY.get(),
				'GENDER_ENTRY': GENDER_ENTRY.get(),
				'SPEED_ENTRY': SPEED_ENTRY.get()
			}
		)

	# commit changes
	db.commit()
	# close the connection
	db.close()
	# clear entry text
	NAME_ENTRY.delete(0, 'end')
	GENDER_ENTRY.delete(0, 'end')
	SPEED_ENTRY.delete(0, 'end')

TITLE = Label(root, text = "SIMPLE GUI APPLICATION")
NAME_LABEL = Label(root, text = "Enter the driver's name: ")
GENDER_LABEL = Label(root, text = "Enter the driver's gender [M/F]: ")
SPEED_LABEL = Label(root, text = "Enter driving speed: ")


NAME_ENTRY = Entry(root)
GENDER_ENTRY = Entry(root)
SPEED_ENTRY = Entry(root)
SUBMIT_BUTTON = Button(root, text = "SUBMIT", bg ="green", fg="white", command = submit_data)
QUIT_BUTTON = Button(root, text = "QUIT", bg ="red", fg="white", command = exit_gui)

NAME_ENTRY.grid(column =2, row = 1)
GENDER_ENTRY.grid(column =2, row = 2)
SPEED_ENTRY.grid(column =2, row = 3)
SUBMIT_BUTTON.grid(column = 1, row = 4, padx = 10, pady = 10, columnspan = 2)
QUIT_BUTTON.grid(column = 1, row = 5, padx = 10, pady = 10, columnspan = 2)

TITLE.grid(column =2, row = 0, padx = 10, pady = 10, columnspan = 2)
NAME_LABEL.grid(column =0, row = 1, padx = 10, pady = 10, columnspan = 2)
GENDER_LABEL.grid(column =0, row = 2, padx = 10, pady = 10, columnspan = 2)
SPEED_LABEL.grid(column =0, row = 3, padx = 10, pady = 10, columnspan = 2)

root.mainloop()
