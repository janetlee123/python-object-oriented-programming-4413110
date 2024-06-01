# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    def __init__(self,title,author,pages,price):
        self.title=title
        self.author=author 
        self.pages=pages
        self.price=price
        self.__secret="This is a secret attribute"

    # TODO: double-underscore properties are hidden from other classes


    # TODO: create a class method
    def getprice(self):
        if hasattr(self,"_discount"):
            return self.price - (self.price*self._discount)
        return self.price
    
    # TODO: create a static method
   
        

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
   # def set_title(self, newtitle):
    #    self.title = newtitle

    #def __init__(self, title):
    #   self.title = title


# TODO: access the class attribute
    def setdiscount(self,amount):
        self._discount  = amount

# TODO: Create some book instances
b1=Book("War and Peace","Leo Tolstoy",1225,39.90)
b2=Book("The Catcher in the Rye", "JD Salinger",234,29.99)

# TODO: Use the static method to access a singleton object
# print(b1.getprice)
# b2.setdiscount(0.25)
# print(b2.getprice())
print(b2._Book__secret)

