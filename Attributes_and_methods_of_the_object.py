class Hous:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        if new_floor >= 1 and new_floor <= self.number_of_floors:
            return new_floor
        else:
            return ('Такого этажа не существует')


h1 = Hous('ЖК ЖелДор', 30)
print(h1.go_to(22))