
def InsertIntoLanguagesCommand(id, language):
    return '''INSERT INTO Languages
       (id, Language) values
       ({}, '{}');'''.format(id, language)


def InsertIntoGenresCommand(genre):
    return '''INSERT INTO Genres
    (id, Genre) values
    ({}, '{}');'''.format(id, genre)


