class Arguments:
    def KeyWordArgumment(self, a, **keyValue):
        self.a = a
        print("The value of a is :" + str(a))
        print(type(keyValue))
        for i in keyValue.keys():
            print("Keys passed inside the keyValue:\t", str(i))
        print()
        print()
        for i in keyValue.values():
            print("Values passed inside the keyValue:\t", str(i))    
objects = Arguments()
objects.KeyWordArgumment(1, Name = 'Python',creator = 'Guido Van Rossum')
