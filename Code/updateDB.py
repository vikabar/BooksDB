import sqlite3
import InsertCommands
import ClearTableCommands

#connect to database
conn = sqlite3.connect('BOOKS.db')
c = conn.cursor()



conn.commit()