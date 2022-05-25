print('Задание №1')
'''
Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
до часа: <m> мин <s> сек;
до суток: <h> час <m> мин <s> сек;
* в остальных случаях: <d> дн <h> час <m> мин <s> сек.
'''


one_minute = 60
one_hour = 3600
one_day = 86400


duration = int(input("Enter time in seconds : "))

if duration < one_minute:
    print(duration,'seconds')

elif duration >= one_minute and duration < one_hour:
    my_min = duration // one_minute
    my_sec = one_hour % duration
    print(my_min,'min',my_sec,'seconds')

elif duration > one_hour and duration < one_day:
    my_hour = duration // one_hour
    duration = duration % one_hour
    my_min = duration // one_minute
    my_sec = duration % one_minute
    print(my_hour,'hour',my_min,'min',my_sec,'sec')

elif duration > one_day :
    my_days = duration // one_day
    duration = duration % one_day
    my_hour = duration // one_hour
    duration = duration % one_hour
    my_min = duration // one_minute
    my_sec = duration % one_minute
    print(my_days,'days',my_hour,'hour',my_min,'min',my_sec,'sec')




print('Задание №2')
'''
Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
1. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. 
Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. 
Внимание: использовать только арифметические операции!
2. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. 
'''

cubes = [x**3 for x in range(1000) if x % 2 != 0]
print('Cоздан список кубов нечётных чисел', cubes)
my_numbers_sum = 0
my_numbers_sum_list = []

for i in range(len(cubes)):
    my_str = str(cubes[i])
    my_list = list(my_str)

    for i in range(len(my_list)):
        my_list[i] = int(my_list[i])

    for i in range(len(my_list)):
        my_numbers_sum = my_numbers_sum + my_list[i]

    if my_numbers_sum % 7 == 0:
        print('Cумму чисел, делящихся на 7 : ',my_numbers_sum)
        my_numbers_sum_list.append(my_numbers_sum)

print('Список чисел, делящихся на 7 (задание 1) : ',my_numbers_sum_list)

cubes = [(x**3)+17 for x in range(1000) if x%2 == 0]
print('Cоздан список кубов нечётных чисел {}'.format(cubes))
my_numbers_sum = 0
my_numbers_sum_list_even_numbers = []

for i in range(len(cubes)):
    my_str = str(cubes[i])
    my_list = list(my_str)

    for i in range(len(my_list)):
        my_list[i] = int(my_list[i])

    for i in range(len(my_list)):
        my_numbers_sum = my_numbers_sum + my_list[i]

    if my_numbers_sum % 7 == 0:
        print('Cумму чисел, делящихся на 7 : ', my_numbers_sum)
        my_numbers_sum_list_even_numbers.append(my_numbers_sum)

print('Список чисел, делящихся на 7 (задание 2) : ',my_numbers_sum_list_even_numbers)



print('Задание №3')

'''
Склонение слова
Реализовать склонение слова «процент» во фразе «N процентов». 
Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
1 процент
2 процента
3 процента
4 процента
5 процентов
6 процентов
...
100 процентов
'''

for i in range(100):
    new_str = str(i+1)
    new_list = list(new_str)
    if int(new_list[-1]) == 1 and i+1 != 11:
        print('{} процент'.format(i + 1))
    elif int(new_list[-1]) > 1 and int(new_list[-1]) <= 4:
        if i + 1 > 10 and i + 1 <= 14:
            print('{} процентов'.format(i + 1))
        else:
            print('{} процента'.format(i + 1))
    else:
        print('{} процентов'.format(i + 1))

