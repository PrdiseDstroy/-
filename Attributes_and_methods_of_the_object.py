class Hous:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    
    def go_to(self, new_floor):
        for i in range(self.number_of_floors):
            if i >= 1 and i <= self.number_of_floors + 1:
                print(i)
        else:
            return ('Такого этажа не существует')

h1 = Hous('ЖК ЖелДор', 30)
print(h1.go_to(12))
