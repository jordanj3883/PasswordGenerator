class password:
    ##making random passwords
    import string
    import poplib
    import random
    numbers_and_letters = list(string.printable) # list of numbers and letters
    symbols = list(string.punctuation) #list of puncuations 
    print(numbers_and_letters)
    length = input("How long of a password")
    count = int(length)
    password  = []
    while count > 0:
        password.append(numbers_and_letters[random.randint(0,len(numbers_and_letters) - 1)])
        count -=1
    printer = ''.join(password)##changes password list to a string
    print(printer)
