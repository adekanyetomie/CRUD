class Toy():
    
    count = 1

    def __init__(self, name):
        self.name = name
        self.id = Toy.count
        Toy.count +=1