import random
n = random.randint(3, 20)
result= ''
for i in range(1, 20):
    for j in range(i + 1, 20):
        if n %(i + j) == 0:
            result += str(i) + str(j)
print(f'Число{n}, пароль{result}')