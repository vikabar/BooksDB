import pandas as pd

PATH_TO_EXCEL = r'C:\Users\vbaranov\personal\books\BooksDB\BOOKS DB2.xlsx'

def clear(txt):
    txt2 = txt.strip('\u200e')
    return txt2


def parse_languages():
    '''languages_array[i][0] --> id(int)
    languages_array[i][1] --> language(str)'''
    languages_array = []
    sheet_name = "Languages"
    languages = pd.read_excel(open(PATH_TO_EXCEL, 'rb'),
                  sheet_name=sheet_name)
    num_of_languages = len(languages)
    for i in range(num_of_languages):
        id = int(languages["Id"][i])
        language = clear(languages["Language"][i])
        print(id, language)
        languages_array.append((id,language))
    return languages_array


def parse_genres():
    '''
    parses genres sheet
    :return: genres_array[i][0] --> id(int)
        genres_array[i][1] --> genre(str)
    '''
    genres_array = []
    sheet_name = "Genres"
    genres = pd.read_excel(open(PATH_TO_EXCEL, 'rb'),
                              sheet_name=sheet_name)
    num_of_genres = len(genres)
    for i in range(num_of_genres):
        id = int(genres["Id"][i])
        genre = clear(genres["Genre"][i])
        genres_array.append((id, genre))
    t = tuple(genres_array)
    return t



'''c.execute(CreateTablesCommands.Genres)
c.execute(CreateTablesCommands.Genders)
c.execute(CreateTablesCommands.Formats)
c.execute(CreateTablesCommands.Authors)
c.execute(CreateTablesCommands.Books)
c.execute(CreateTablesCommands.BookAuthorLinking)
c.execute(CreateTablesCommands.Series)
c.execute(CreateTablesCommands.BookSeriesLinking)
c.execute(CreateTablesCommands.BooksIOwn)
c.execute(CreateTablesCommands.BookGenreLinking)
c.execute(CreateTablesCommands.BooksIveRead)'''

#l = parse_languages()
g = parse_genres()
print()