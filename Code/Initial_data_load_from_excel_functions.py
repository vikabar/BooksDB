import sqlite3
import ParsingExcel
import InsertCommands


def import_languages():
    commands_list = []
    data = ParsingExcel.parse_languages()
    for row in data:
        id = row[0]
        language = row[1]
        command = InsertCommands.InsertIntoLanguagesCommand(id, language)
        commands_list.append()
        



conn = sqlite3.connect('BOOKS.db')
c = conn.cursor()




conn.commit()