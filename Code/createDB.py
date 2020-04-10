import sqlite3
import CreateTablesCommands

#connect to database
conn = sqlite3.connect('BOOKS.db')
c = conn.cursor()

c.execute(CreateTablesCommands.Languages)
c.execute(CreateTablesCommands.Genres)
c.execute(CreateTablesCommands.Genders)
c.execute(CreateTablesCommands.Formats)
c.execute(CreateTablesCommands.Authors)
c.execute(CreateTablesCommands.Books)
c.execute(CreateTablesCommands.BookAuthorLinking)
c.execute(CreateTablesCommands.Series)
c.execute(CreateTablesCommands.BookSeriesLinking)
c.execute(CreateTablesCommands.BooksIOwn)
c.execute(CreateTablesCommands.BookGenreLinking)
c.execute(CreateTablesCommands.BooksIveRead)

conn.commit()