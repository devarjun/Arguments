class Arguments:
    def nonKeyWordArgumment(self, a, *num):
        self.a = a
        print("The value of a is :" + str(a))
        print(type(num))
        for i in num:
            print("*Argument passed is:\t", str(i))
            
objects = Arguments()
objects.nonKeyWordArgumment(1, 'This', 'is', 'an',
                            'example', 'of', 'nonKeyWordArgumment' )
