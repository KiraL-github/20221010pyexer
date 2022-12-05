# Create class
class User:
# "c"lass -> is keyword
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1

# Customer class
class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
    # build a function within the class
    def set_balance(self, balance):
        self.balance = balance
    # return f-string template literal
    def greeting(self):
        return 'My name is {0} and I am {1} and I owe a balance of {2}'.format(self.name, self.age, self.balance)

        return f'My name is {self.name} and I am {self.age} and I owe a balance of {self.balance}'

    # or 'My name {0} and I am {1} and I owe a balance of {2}'.format(self.name, self.age, self.balance)

    # create user based on the class
    aaron = User('Aaron Wai ', 'awai@gmail.com', 37)
    may = User('May Chan', 'may@gmail.com', 27)

    # Edit internal variable
    aaron.age = 38

    # run internal function
    may.has_birthday()

    # Call method
    print(may.greeting())

    # create customer based on customer class
    john = Customer('John chan', 'john@gmail.com', 40)

    # call internal function