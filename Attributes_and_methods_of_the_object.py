class Hous:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
            if new_floor >= 1 and new_floor <= self.number_of_floors:
                for i in range(1, new_floor + 1):
                    print(i)
            else:
                print('Такого этажа не существует')

h1 = Hous('ЖК ЖелДор', 22)
h1.go_to(13)
