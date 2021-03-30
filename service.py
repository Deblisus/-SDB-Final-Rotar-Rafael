from entities import Book

class Service():
    def __init__(self):
        ''' Constructor '''

        self.__books = []

    def get_all_books(self):
        ''' Returneaza o lista cu toate cartile inregistrate '''

        return self.__books
    
    def initialize_default_books(self):
        self.__books.append(Book("Ion", "Liviu Rebreanu", 1920, 20))
        self.__books.append(Book("Moara cu noroc", "Ioan Slavici", 1881, 50))
        self.__books.append(Book("Hronicul si cantecul varstelor", "Lucian Blaga", 1965, 120)),
        self.__books.append(Book("Hanu Ancutei", "Mihail Sadoveanu", 1928, 37))



    def add_book(self, new_book):
        ''' Adauga o carte noua in lista

            return: returneaza 1 in cazul in care cartea a fost adaugata cu succes sau
                    -1 in cazul in care cartea deja exista
            new_book: cartea pentru adaugat
         '''

        for book in self.__books:
            if new_book == book:
                return -1
        
        self.__books.append(new_book)
        return 1

    def update_book_by_title(self, title, author, age, price):
        ''' Updateaza o carte dupa titlu

            return: returneaza 1 in cazul in care cartea a fost updatata cu succes sau
                    -1 in cazul in care cartea nu exista
            title: Identificatorul dupa care se va updata cartea
            author: Autorul pentru updatat
            age: Anul pentru updatat
            price: Pretul pentru updatat
         '''

        pos = find_pos(title, self.__books)
        if pos == -1:
            return -1
        
        self.__books[pos].update_by_title(author, age, price)
        return 1
    
    def delete_book_by_title(self, title):
        ''' Sterge o carte dupa titlu 

            return: returneaza 1 in cazul in care cartea a fost stearsa cu succes sau
                    -1 in cazul in care cartea nu exista
            title: Identificatorul dupa care se va efectua stergerea
        '''

        pos = find_pos(title, self.__books)
        if pos == -1:
            return -1
        
        del self.__books[pos]
        return 1


# Other functions

def find_pos(title, books):
    ''' Gaseste pozitia  unei carti folosind titlul
        return: pozitia cartii in lista sau -1 in cazul in care cartea nu exista
     '''

    for i in range(len(books)):
        if title == books[i].get_title():
            return i
    return -1