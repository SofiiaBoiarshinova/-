#Напишите **рекурсивную** функцию ```fact```, которая вычисляет факториал заданного числа ```x```.
def fact(n):
    if (n <= 1):
        return 1
    else:
        return (n * fact(n-1))

#2 Создайте функцию ```filter_even```, которая принимает на вход список целых чисел,  и фильтруя, возвращает список, содержащий только четные числа. Используйте ```filter``` для фильтрации и  ```lambda```.
def filter_even(l):
    return list(filter(lambda x: x % 2 == 0, l))
#3 Напишите функцию ```square``` ,которая принимает на вход список целых чисел и возвращает список с возведенными в квадрат элементами. Используйте ```map```.
def square(list):
    res = [i**2 for i in map(int, list.split())]
    return res
#4 Напишите функцию бинарного поиска ```bin_search```, которая принимает на вход отсортированный список и элемент. Функция должна возвращать индекс искомого элемента в списке. 
def bin_search(list, n):
    start = 0
    end = len(list)
    while start <= end:
        mid = (start+end)//2
        if list[mid] == n:
            return mid
        if n < list[mid]:
            end = mid-1
        else:
            start = mid+1
    return -1
#5 Напишите функцию ```is_palindrome``` определяющую,является ли строка палиндромом. Палиндромами являются текстовые строки, которые одинаково читаются слева направо и справа налево. В строках не учитываются знаки препинания, пробельные символы и цифры; регистр не имеет значения. 

def is_palindrome(x):
 x = len(word)
 i = 0
 x = x - 1
 k = 0
 while x - i >= i:
      if word[x - i] == word[i]:
          i += 1
      else:
          k = 1
          break
 if k == 1:
    print("no")
 else:
    print("yes")
#6 Написать функцию ```calculate```, которая принимает на вход текстовый файл содержащий строки следующего формата: etc
OPS = {'+': lambda x, y: x + y, '-': lambda x, y: x - y,
       '*': lambda x, y: x * y, '//': lambda x, y: x//y,
       '%': lambda x, y: x % y,  '**': lambda x, y: x ** y}


def load_file(filename):
    file = open(filename, encoding='utf-8')
    data = [line.strip().split('    ') for line in file.readlines()]
    file.close()
    return data


def evaluate(l_number, r_number, op):
    if op in OPS:
        return OPS[op](l_number, r_number)
    else:
        print('Неизвестная операция')


def calculate(path2file):
    data = load_file(path2file)
    operation = 0
    f_operand = 1
    s_operand = 2
    result = []
    for exp in data:
        result.append(str(evaluate(int(exp[f_operand]), int(exp[s_operand]), exp[operation])))
    return ','.join(result)


def main_():
    data = calculate('test_input_file_1.txt')
    print(data)


main_()

#7Написать функцию ```substring_slice```,которой на вход поступают два текстовых файла. 
# - Первый файл содержит строки текста.   
# - Второй файл содержит строки из двух целых неотрицательных чисел.
#Первое число в строке всегда меньше или равно второму.
#Числа всегда меньше длины соответствующей строки первого файла.
#Соответствующей - это значит 1-ая строка из 1-го файла соответствует 1-ой строке из 2-го файла, а 123-я строка из 1-го файла соответствует 123-ей строке из 2-го файла.

#- Функция должна вернуть строку, состоящую из подстрок 1-го входного файла.
#Подстроки разделены пробелами.
#Какие брать подстроки - написано во втором файле.
#В конце файла пробела нет.
def load_file(filename):
    file = open(filename, encoding='utf-8')
    data = [line for line in file.readlines()]
    file.close()
    return data


def substring_slice(path2file_1, path2file_2):
    data_1 = load_file(path2file_1)
    data_2 = load_file(path2file_2)
    result = []
    for line_1, line_2 in zip(data_1, data_2):
        start_index, end_index = map(int, line_2.strip().split())
        result.append(line_1[start_index:end_index + 1])
    return ' '.join(result)
#8 Написать функцию ```decode_ch```,на вход которой поступает строка.В ней хранится набор химических символов (He, O, H, Mg, Fe, ...). Без пробелов. Нужно расшифровать химические символы в название химических элементов.Функция должна вернуть строку - расшифровку.
import json


def decoded_ch(string_of_elements):
    periodic_table = json.load(open('periodic_table.json', encoding='utf-8'))
    search_index = 1
    result = ''
    while string_of_elements:
        last_ch = string_of_elements[search_index:search_index + 1].isupper()\
            if string_of_elements[search_index:search_index + 1] else True
        if string_of_elements[:search_index] in periodic_table and last_ch:
            result += periodic_table[string_of_elements[:search_index]]
            string_of_elements = string_of_elements[search_index:]
            search_index = 1
        else:
            search_index += 1
    return result

#9Создайте класс с названием Student.
#При инициализации объекта подается два аргумента. Первый - имя студента. Второй - фамилия студента.

#1. Создайте три атрибута объекта данного класса:

#- *name* имя студента
#- *surname* фамилия студента
#- *fullname* имя и фамилия студента через пробел
#2. Создайте метод для экземпляра класса Student под названием greeting, который при вызове возвращает строку Hello, I am Student
#Здесь и далее нужно только написать сам класс. 
#3. Добавьте новый атрибут класса под названием grades. При инициализации объекта соответственно добавляется новый аргумент, в котором будет лежать список оценок данного студента, по дефолту равный списку [3,4,5]. Создайте метод под названием mean_grade, который возвращает среднее всех оценок студента (то есть среднее этого атрибута).
#4. Сделайте метод is_otlichnik, который возвращает строку YES, если средняя оценок студента больше или равна 4.5 и NO в противном случае.
#Примечание: этот метод должен вызывать метод mean_grade внутри себя.
#5. На этот раз определим операцию сложения для двух студентов. Пусть такая операция возвращает строку следующего вида: "Name1 is friends with Name2", где Name1 и Name2 - имена первого студента и второго (именно атрибут name). То есть, если создать два экземпляра класса Student, то их сумма должна вернуть вышеописанную строку.
#6. Теперь переопределим поведение нашего класса с функцией print. Пусть при вызове функции print от экземпляра класса Student печатается его атрибут fullname.
class Student:
    def __init__(self, name, surname, grades=None):
        self.name = name
        self.surname = surname
        self.fullname = name + ' ' + surname
        if grades is None:
            grades = [3, 4, 5]
        self.grades = grades

    def is_otlichnik(self):
        return 'Yes' if self.mean_grades() >= 4.5 else 'NO'

    def greeting(self):
        return f'Hello, I am {self.fullname}'

    def mean_grades(self):
        return sum(self.grades)/len(self.grades)

    def __add__(self, other):
        return f'{self.name} is friends with {other.name}'

    def __str__(self):
        return self.fullname


def main_1():
    student_1 = Student('Bobb', 'Greeny', [4,5,5])
    student_2 = Student('Stevee', 'Brrown')
    print(student_1.greeting())
    print(student_2)
    print(student_1.is_otlichnik())
    print(student_1 + student_2)


main_1()

#10

#Определите  класс исключений ```MyError```,
 #который принимает строковое сообщение ```msg``` в качестве параметра при инициализации и также имеет атрибут ```msg```.

#Подсказка: Чтобы определить кастомный класс  исключения,нужно создавать класс, унаследованный от ```Exception```.
class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(msg)


raise MyError('error')