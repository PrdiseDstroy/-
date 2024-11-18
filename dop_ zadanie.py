n = [14, 5]
result= ''
result_1 = ''
for i in range(1, 30):
    for j in range(i + 1, 30):
        if (i + j) % n[1] == 0:
            if n[1] != i + j:
                result += str(i) + str(j)
            for k in range(i + j + 1, 30):
                if n[0] % (i + j + k) == 0:
                    result_1 += str(i) + str(j) + str(k)
print(f'Число {n[1]}, пароль {result}')
print(f'Число {n[0]}, пароль {result_1}')