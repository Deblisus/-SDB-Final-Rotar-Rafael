from service import Service
from entities import Book

class UI():
    def __init__(self, service):
        ''' Constructor 

            service: serviciul pentru aplicatie
        '''

        self.__service = service

    

    def __add_book(self):
        print("\n")

        title = input("Introduceti titlul cartii: ")
        author = input("Introduceti autorul cartii: ")
        age = int(input("Introduceti anul publicarii cartii (aveti grija sa fie un numar ;): "))
        price = float(input("Introduceti pretul cartii (aveti grija sa fie un numar ;): "))

        new_book = Book(title, author, age, price)
        res = self.__service.add_book(new_book)

        if res == -1:
            print("\nCartea exista deja!\n")
        else:
            print("\nCartea a fost adaugata cu succes!\n")

    def __print_books(self):
        books = self.__service.get_all_books()
        print("\n")
        print(books)
        print("\n")
    
    def __update_book(self):
        print("\n")

        title = input("Introduceti titlul cartii pe care doriti sa o updatati: ")
        author = input("Introduceti autorul nou al cartii: ")
        age = int(input("Introduceti anul nou al cartii (deja stiti povestea ;): "))
        price = float(input("Introduceti pretul nou al catrii (la fel si aici): "))

        res = self.__service.update_book_by_title(title, author, age, price)

        if res == -1:
            print("\nCartea nu exista!\n")
        else:
            print("\nCartea a fost updatata cu succes!\n")
    
    def __delete_book(self):
        print("\n")

        title = input("Introduceti titlul cartii pe care doriti sa o stergeti: ")

        res = self.__service.delete_book_by_title(title)

        if res == -1:
            print("\nCartea nu exista!\n")
        else:
            print("\nCartea a fost stearsa cu succes!\n")

    
    

    def __print_menu(self):
        print("0. Iesiti din aplicatie")
        print("1. Afiseaza toate cartile din lista")
        print("2. Adauga o carte noua")
        print("3. Modifica o carte dupa nume")
        print("4. Sterge o carte dupa nume")

    def run(self):
        options = {
            '1': self.__print_books,
            '2': self.__add_book,
            '3': self.__update_book,
            '4': self.__delete_book,
        }
        self.__service.initialize_default_books()

        while True:
            self.__print_menu()
            command = input("\nIntroduceti comanda dorita: ")
            
            if command == '0':
                break
            elif not(command in options):
                print("\nComanda invalida!\n")
            else:
                options[command]()

