# Задача 1. Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи. 6 –> 1 1 2 3 5 8


N = int(input('Введите число: '))


def fib(n):
     if n in [1, 2]:
         return 1
     else:
         return fib(n-1) + fib(n-2)


list = []
for e in range(1, N+1):
     list.append(fib(e))

data = open('fibo.txt', 'w')
data.write(str(list))
data.close()

    # Задача 2. В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву. а –> абрикос, авокадо, апельсин, айва.

letterN = input('Введите букву: ')
 #letter = ''
path = 'frukt.txt'
data = open(path, 'r')
for line in data:
     #letter = line
     if letterN == line[0]:
         print(line)
data.close()

# Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут». Если фраза ему неизвестна, он выводит соответствующую фразу.

dictionary = \
     {
         'привет': 'привет!',
         'как тебя зовут': 'меня зовут Роби',
         'else': 'Не понимаю о чем речь...'
     }
phrase = str(input('>>> '))
flag = 0
for i in dictionary.keys():
     if i in phrase:
         print(dictionary[i])
         flag = 1
if flag == 0:
     print(dictionary['else'])

