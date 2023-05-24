'''Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы'''
def PrintOperationTable(operation, numrows,numcolumns):
    lst1= [i for i in range (1, numcolumns+1)]
    #print(lst1)
    for j in range (1, numrows+1):
        lst2 = [operation(i,j) for i in lst1]
        #print(lst2)
        print(*lst2,sep='\t')
        
rows = 6
columns = 5

PrintOperationTable(lambda x,y: x*y, rows, columns)   





# a = [[1,2,3,4,5],[1,2,3,4,5,6]]
# # def operation(num_rows,num_columns):
# #    for x in range(num_rows):
# #        for y in range(num_columns): 
# #             print(*z(x+1),(y+1),'\n')
# # mas = [[x] for x in range a, y in range b]
# # num_rows=6 
# # num_columns=6        
# # print_operation_table(operation, z(5,6)
# for i in range(len(a[0])):
#     for j in range(len(a[1])):
#         print(a[i][j], end=' ')
#     print()
# m=5
# n=6
# s = [[i * j for j in range(m)] for i in range(n)]
# print((*s[i],'\n') for i in range n)
