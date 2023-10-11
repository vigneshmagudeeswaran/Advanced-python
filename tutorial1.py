class Dog(object):
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def speak(self):
       print('Hi I am', self.name, 'and I am', self.age, 'years old')

    def change_age(self, age):
        self.age = age
    def add_weight(self, weight):
        self.weight = weight
    
        
tim = Dog('Tim', 55)
tim.speak()
tim.change_age(5)
tim.speak()
print(tim.age)
tim.add_weight(70)
print(tim.weight)

    
    