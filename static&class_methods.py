class Dog(object):
    
    dogs = [] # class variables
    x = 5
    
    def __init__(self,name):
        self.name = name
        self.dogs.append(self)
    
    @classmethod
    def num_dogs(cls):
       return len(cls.dogs)

    @staticmethod
    def bark(n):
        """barks n times"""
        for _ in range(n):
            print("bark")
            
tim = Dog('Tim')
jim = Dog('Jim')
print(Dog.dogs)
print(Dog.num_dogs())# class method
print(Dog.bark(5))
    

    
    
        



    
    