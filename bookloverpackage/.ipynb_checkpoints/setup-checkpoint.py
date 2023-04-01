from setuptools import setup, bookloverpackage

setup(
    name='bookloverpackage',
    version='1.0.0',
    url='https://github.com/cestrawley/M09_Homework',
    author='Catherine Strawley',
    author_email='ces9ra@virginia.edu',
    description='Contains a BookLover class that allows a user to add books and ratings to a book list and determine the number of books read, favorite books based on ratings, and whether a book to add to the list has already been read. The package also contains a class BookLover_Test to perform unit tests on booklover.',
    packages=[bookloverpackage], 
    install_requires=['numpy >= 1.11.1', 'pandas'],
)