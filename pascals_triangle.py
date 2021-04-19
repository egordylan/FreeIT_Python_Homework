print('''Написать функцию, которая выводит на экран треугольник Паскаля
заданной высоты.''')

rows = int(input())

def TrianglePascale(rows):
    row = [1]
    for i in range(rows):
        print(row)
        row = [sum(x) for x in zip([0] + row, row + [0])]

TrianglePascale(rows)
