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
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'Название "{self.name}", кол-во этажей {self.number_of_floors} '

    def __eq__(self, other):
        return  self.number_of_floors == other.number_of_floors
    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors


    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
    def __iadd__(self, other):
        if isinstance(other, int):
            return self



h1 = Hous('ЖК ЖелДор', 20)
h2 = Hous('ЖК Реутово', 21)
h3 = Hous('ЖК Салтыковская', 23)
h1 = h1 +3
h1.go_to(13)

print(h1)
print(len(h1))
print(h1 == h2)
print(h2 < h1)
print(h2 <= h3)
