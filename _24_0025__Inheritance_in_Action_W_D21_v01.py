class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")

class Fish(Animal):
    def __init__(self):    #add the initializer
        super().__init__()

    def breathe(self):
        super().breathe()      #to modify a Method from another Class. super(). + the Method() name from the other Class
        print("doing this underwater")     # and you can add unique modifications to the .breathe() Method

    def swim(self):
        print("moving in water")

nemo = Fish()
nemo.swim()

nemo.breathe()   #addition to check functionality
# moving in water
# Inhale, exhale         # this was inherited from another Class !!!
# doing this underwater      # this Method was inheritated from another Class !!!

print(nemo.num_eyes)
# 2                       # this was inherited from another Class !!!
