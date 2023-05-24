'''Задача 34:  Винни-Пух '''
'''Variant 2'''
z = 'пари-ро-рам рем-пам-пупам па-ры-па-дя'
g = 'аиеёоуыэюя'
res = list()
count = 0
for i in z.split():
    for j in i:
        if j in g: 
            count+=1
    res.append(count)
    print(res)
    count = 0
print('Парам пам-пам' if max(res) == min(res) else 'Пам парам')