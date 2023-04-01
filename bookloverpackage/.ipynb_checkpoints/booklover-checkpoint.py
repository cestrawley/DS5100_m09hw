import pandas as pd
import numpy as np

class BookLover():
    '''
    The BookLover class includes attributes of the name of a person (string), the person's email (string), their favorite book genre (string); all of which require entry from the user. Additional attributes include the number of books the person has read (integer), as well as a dataframe called book_list that contains information about the books they have read (including book title and rating 0-5); these additional attributes are optional for the user to enter. The class contains 4 additional methods. 1) add_book() allows the user to enter the name of a book they have read and a corresponding rating, and then adds the book and rating to the book_list dataframe if the book is not already in it. 2) has_read() takes a book name as input from the user and returns true if the person has read the book (based on contents of the book_list dataframe) and false if they have not. 3) num_books_read() returns the number of books read based on the number of books present in the book_list dataframe. 4) fav_books() returns a dataframe of the person's favorite books, based on those present in the book_list dataframe with ratings>3.
    '''

    def __init__(self,name,email,fav_genre,num_books = 0,book_list = pd.DataFrame({'book_name':[],'book_rating':[]})):
        '''initializes attributes of the name of a person (string), the person's email (string), their favorite book genre (string); all of which require entry from the user. Additional attributes include the number of books the person has read (integer), as well as a dataframe called book_list that contains information about the books they have read (including book title and rating 0-5); these additional attributes are optional for the user to enter. '''
        self.name=str(name)
        self.email=str(email)
        self.fav_genre=str(fav_genre)
        self.num_books=int(num_books)
        self.book_list=book_list
   
    
    def add_book(self,book_name,book_rating):
        '''allows the user to enter the name of a book they have read and a corresponding rating, and then adds the book and rating to the book_list dataframe if the book is not already in it'''
        self.book_name=str(book_name) #self
        self.book_rating=int(book_rating)
        new_book = pd.DataFrame({
                'book_name': [self.book_name],#self
                'book_rating': [self.book_rating]
            })
        if (self.book_list['book_name'].eq(self.book_name)).any():
            return 'this book is already in your list'
        else:
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.book_list.loc[self.book_list['book_rating']>=5, 'book_rating'] = 5
            self.book_list.loc[self.book_list['book_rating']<=0, 'book_rating'] = 0 
            self.num_books +=1

            
    def has_read(self,book_name):
        '''takes a book name as input from the user and returns true if the person has read the book (based on contents of the book_list dataframe) and false if they have not'''
        self.book_name=str(book_name)
        if (self.book_list['book_name'].eq(self.book_name)).any():
            return True
        else:
            return False
    
    
    def num_books_read(self):
        '''returns the number of books read based on the number of books present in the book_list dataframe'''
        return self.num_books
        #should equal value of return len(book_list)
   

    def fav_books(self):
        '''returns a dataframe of the person's favorite books, based on those present in the book_list dataframe with ratings>3'''
        return self.book_list[self.book_list['book_rating']>3]
        #return self.book_list[self.book_list.book_rating >3]