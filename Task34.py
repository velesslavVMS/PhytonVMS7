'''Задача 34:  Винни-Пух '''
#z = input().split()
z = 'пара-ра-рам рам-пам-папам па-ра-па-да'
w = z.split()
w = ['па-ра-ра-рам', 'рам-пам-папам', 'па-ра-па-дапа']
#w = 'па-ра-ра-рам'
print(w)
#g = 'аиеёоуыэюя'
c = [i.count('а') for i in w]
print(c)
q1 = sum(c)
print(q1)
q2 = c[0]*len(c)
print(q2)
print('Парам пам-пам' if q1==q2 else 'Пам парам')