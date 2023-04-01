import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    '''
    The BookLoverTestSuite() class performs unit testing on an imported class, BookLover. The class contains 6 test methods to assess the functionality (and look for errors) in the BookLover class. These test methods are as follows: 1) test_1_add_book method to add a book and test if it is in book_list. 2) test_2_add_book() method to add the same book twice and test if it's in book_list only once. 3) test_3_has_read() method to pass a book in the list and test if the returned value of the BookLover class' has_read() method is True. 4) test_4_has_read() method to pass a book NOT in the list and use assert False to test if the answer when running the BookLover class' has_read() method is True. 5) test_5_num_books_read() method to add some books to the list, and test num_books matches expected. 6) test_6_fav_books() method to add some books with ratings to the book list, making sure some of them have rating >3 and check that the returned books have rating >3 when BookLover class' fav_books() method is run.
    '''
    
    def test_1_add_book(self):
        '''method to add a book and test if it is in book_list'''
        booklover1 = BookLover('Catherine','ces9ra@virginia.edu','Non-fiction')
        booklover1.add_book('The Great Gatsby',4)
        test1_val = 'The Great Gatsby' in booklover1.book_list['book_name'].values
        error_message1 = 'The book was not added successfully to the list'
        self.assertTrue(test1_val, error_message1)

    def test_2_add_book(self):
        '''method to add the same book twice and test if it's in book_list only once'''
        booklover1 = BookLover('Catherine','ces9ra@virginia.edu','Non-fiction')
        booklover1.add_book('The Great Gatsby',4)
        booklover1.add_book('The Great Gatsby',4)
        test2_val = (len(booklover1.book_list[booklover1.book_list['book_name']=='The Great Gatsby']))
        error_message2 = 'The book was added more than once'
        self.assertEqual(test2_val,1,error_message2)        
   
    def test_3_had_read(self):
        '''method to pass a book in the list and test if the returned value of the BookLover class' has_read() method is True'''
        booklover1 = BookLover('Catherine','ces9ra@virginia.edu','Non-fiction')
        booklover1.add_book('The Great Gatsby',4)
        test3_val = booklover1.has_read('The Great Gatsby')
        error_message3 = 'The method incorrectly indicated that a book that had been read had not been read'
        self.assertTrue(test3_val,error_message3)
        
    def test_4_has_read(self):
        '''method to pass a book NOT in the list and use assert False to test if the answer when running the BookLover class' has_read() method is True'''
        booklover1 = BookLover('Catherine','ces9ra@virginia.edu','Non-fiction')
        booklover1.add_book('The Great Gatsby',4)
        test4_val = booklover1.has_read('To Kill a Mockingbird')
        error_message4 = 'The method incorrectly indicated that a book that had not been read was read'
        self.assertFalse(test4_val,error_message4)
    
    def test_5_num_books_read(self):
        '''method to add some books to the list, and test num_books matches expected'''
        booklover1 = BookLover('Catherine','ces9ra@virginia.edu','Non-fiction')
        booklover1.add_book('To Kill a Mockingbird',4)
        booklover1.add_book('1984',4)
        numbooks_expected=2
        error_message5='The calculated number of books in the list is not equal to the number of books expected based on number of entries'
        self.assertEqual(booklover1.num_books_read(),numbooks_expected,error_message5)
    
    def test_6_fav_books(self):
        '''method to add some books with ratings to the book list, making sure some of them have rating >3 and check that the returned books have rating >3 when BookLover class' fav_books() method is run'''
        booklover1 = BookLover('Catherine','ces9ra@virginia.edu','Non-fiction')
        booklover1.add_book('Beloved',4)
        booklover1.add_book('Thinking Fast and Slow',5)
        expected_val = 2
        test6_val = (len(booklover1.book_list[booklover1.book_list['book_rating']>3]))
        error_message6='Book ratings are not correctly stored'
        self.assertEqual(test6_val,expected_val,error_message6)
        
if __name__ == '__main__':
    unittest.main(verbosity=3)