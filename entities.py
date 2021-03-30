class Book():
    def __init__(self, title, author, age, price):
        ''' Constructor '''

        self._title = title
        self._author = author
        self._age = age
        self._price = price
    
    def update_by_title(self, author, age, price):
        ''' Updateaza o carte dupa titlu '''
        
        self._author = author
        self._age = age
        self._price = price

    
    # Getters

    def get_title(self):
        ''' Getter titlu '''

        return self._title

    def get_author(self):
        ''' Getter autor '''

        return self._author
    
    def get_age(self):
        ''' Getter an '''

        return self._age

    def get_price(self):
        ''' Getter pret '''

        return self._price

    
    # Setters

    def set_title(self, title):
        ''' Setter titlu 
            title: titlul schimbat
        '''

        self._title = title

    def set_author(self, author):
        ''' Setter autor 
            author: autorul schimbat
        '''

        self._author = author

    def set_age(self, age):
        ''' Setter an 
            age: anul schimbat
        '''

        self._age = age

    def set_price(self, price):
        ''' Setter pret 
            price: pretul schimbat
        '''

        self._price = price


    #
    
    def __repr__(self):
        ''' Suprascrie functia str '''

        return "[Titlu: {0}, Autor: {1}, an: {2}, pret: {3}]\n".format(self._title, self._author, self._age, self._price)
    
    def __eq__(self, other):
        ''' Suprascrie operator == '''

        return other.get_title() == self._title and other.get_author() == self._author and other.get_age() == self._age and other.get_price() == self._price