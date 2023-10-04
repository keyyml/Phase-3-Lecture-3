# define a class Book with 4 properties: title, author, page_count
# define a class attribute all that stores all objects
    # when should this attribute be initialized? when should it be used?
# define 3 class methods: get_all_books that returns all books,
#                         get_avg_page_count that returns the mean page count
#                         get_longest that returns the longest book
    # what are two ways of defining these class methods?

class Book:

    all = []

    def __init__(self, title, author, page_count):
        self._title = title
        self._author = author
        self._page_count = page_count

        Book.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if type(title) == str:
            self._title = title
        else:
            raise Exception("The title must be a string!")
        
    @property 
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if type(author) == str and len(author) > 4:
            self._author = author
        else: 
            raise Exception("Author name must be longer")
        
    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count):
        if type(page_count) == int and page_count > 0:
            self._page_count = page_count
        else: 
            raise Exception("Page Count must be a positive integer!")
    
    #class methods
    def get_all_books():
        return Book.all
    
    @classmethod #cls refers to the entire class like self refers to each book
    def get_longest(cls):
        max_page_count = 0
        max_page_count_book = None

        for book in cls.all:
            page_count = book.page_count 
            if page_count > max_page_count:
                max_page_count = page_count
                max_page_count_book = book

        return max_page_count_book
    
    @classmethod
    def get_avg_pg_count(cls):
        #sum of page_count / number of books

        # sum_page_counts = 0
        
        # for book in cls.all:
        #     sum_page_counts = sum_page_counts + book.page_count
        
        # avg = sum_page_counts / len(cls.all)
        avg = sum([book.page_count for book in cls.all]) / len(cls.all)

        return avg

        
    def __repr__(self):
        return(f"Title: {self.title}\nAuthor: {self.author}\nPage Count: {self.page_count}\n")
    
        
twilight = Book("Twilight", "Stephanie Meyer", 430)
new_moon = Book("New Moon", "Stephanie Meyer", 375)
eclipse = Book("Eclipse", "Stephanie Meyer", 500)
breaking_dawn = Book("Breaking Dawn", "Stephanie Meyer", 520)

# Book.all.append(twilight)
# print(Book.all)
# print([book.page_count for book in Book.all])
# print(Book.get_all_books())
print(Book.get_longest())
print(Book.get_avg_pg_count())



# twilight.page_count = 1000
# print(twilight.title)
# print(twilight.page_count)