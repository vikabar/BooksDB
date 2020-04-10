
Languages = '''CREATE TABLE IF NOT EXISTS Languages (
    [id] integer PRIMARY KEY,
    [Language] text NOT NULL
)'''

Genres = '''CREATE TABLE IF NOT EXISTS Genres (
    [id] integer PRIMARY KEY,
    [Genre] text NOT NULL
)'''

Genders = '''CREATE TABLE IF NOT EXISTS Genders (
    [id] integer PRIMARY KEY,
    [Gender] text NOT NULL
)'''

Formats = '''CREATE TABLE IF NOT EXISTS Formats (
    [id] integer PRIMARY KEY,
    [Format] text NOT NULL
)'''

Authors = '''CREATE TABLE IF NOT EXISTS Authors (
    [id] integer PRIMARY KEY,
    [FirstNameHebrew] text,
    [LastNameHebrew] text,
    [FirstNameEnglish] text,
    [LastNameEnglish] text,
    [PseudonymHebrew] text,
    [PseudonymEnglish] text,
    [GenderID] integer,
    FOREIGN KEY (GenderID) REFERENCES Genders (id)
)'''

Books = '''CREATE TABLE IF NOT EXISTS Books (
    [id] integer PRIMARY KEY,
    [Name] text NOT NULL,
    [NameInEnglish] text,
    [NameInHebrew] text,
    [WrittenInLanguageID] integer,
    [Year] integer,
    FOREIGN KEY (WrittenInLanguageID) REFERENCES Languages (id)
)'''

Series = '''CREATE TABLE IF NOT EXISTS Series (
    [id] integer PRIMARY KEY,
    [Name] text NOT NULL,
    [NameInEnglish] text,
    [NameInHebrew] text,
    [Length] integer
)'''

BooksIOwn = '''CREATE TABLE IF NOT EXISTS BooksIOwn (
    [id] integer PRIMARY KEY,
    [BooksID] integer NOT NULL,
    [MyCopyLanguage] integer NOT NULL,
    [MyCopyFormat] integer NOT NULL,
    FOREIGN KEY (BooksID) REFERENCES Books (id),
    FOREIGN KEY (MyCopyLanguage) REFERENCES Languages (id),
    FOREIGN KEY (MyCopyFormat) REFERENCES Formats (id)
)'''

BooksIveRead = '''CREATE TABLE IF NOT EXISTS BooksIveRead (
    [id] integer PRIMARY KEY,
    [BooksID] integer NOT NULL,
    [ReadingLanguage] integer NOT NULL,
    [ReadingFormat] integer NOT NULL,
    [ReadingDate] date,
    [ReadingGrade] integer,
    FOREIGN KEY (BooksID) REFERENCES Books (id),
    FOREIGN KEY (ReadingLanguage) REFERENCES Languages (id),
    FOREIGN KEY (ReadingFormat) REFERENCES Formats (id)
)'''


BookSeriesLinking = '''CREATE TABLE IF NOT EXISTS BookSeriesLinking (
    [id] integer PRIMARY KEY,
    [BookID] integer NOT NULL,
    [SeriesID] integer NOT NULL,
    [NumInSeries] integer NOT NULL,
    FOREIGN KEY (BookID) REFERENCES Books (id),
    FOREIGN KEY (SeriesID) REFERENCES Series (id)
)'''
BookAuthorLinking = '''CREATE TABLE IF NOT EXISTS BookAuthorLinking (
    [id] integer PRIMARY KEY,
    [BookID] integer NOT NULL,
    [AuthorID] integer NOT NULL,
    FOREIGN KEY (BookID) REFERENCES Books (id),
    FOREIGN KEY (AuthorID) REFERENCES Authors (id)
)'''
BookGenreLinking = '''CREATE TABLE IF NOT EXISTS BookGenreLinking (
    [id] integer PRIMARY KEY,
    [BookID] integer NOT NULL,
    [GenreID] integer NOT NULL,
    FOREIGN KEY (BookID) REFERENCES Books (id),
    FOREIGN KEY (GenreID) REFERENCES Genres (id)
)'''