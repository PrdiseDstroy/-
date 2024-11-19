n = [14, 5]
print(type(n))
result= []
for i in range(1, 30):
    res=[]
    for j in range(i + 1, 30):
        if (i + j) % n[1] == 0:
            if n[1] != i + j:
                result += str(i) + str(j)
result_1 = []
for i in range(1, 30):
    res_1=[]
    for j in range(i + 1, 30):
        for k in range(i + j + 1, 30):
            if n[0] % (i + j + k) == 0:
                res_1 += str(i) + str(j) + str(k)
                result_1.append(res_1)
print(f'Число {n[1]}, пароль {result}')
print(f'Число {n[0]}, пароль {result_1}')
