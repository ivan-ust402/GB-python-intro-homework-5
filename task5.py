"""
5) Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
выводить ее на экран.
"""
try:
    with open("file_for_fifth_task.txt", "w+", encoding="UTF-8") as file_object:
        line = input("Введите цифры через пробел: ")
        file_object.writelines(line)
        list_of_numbers = line.split()
        print(sum(map(int, list_of_numbers)))
except IOError:
    print("Ошибка ввода-вывода")
except ValueError:
    print("Вы ввели неправильные значения")
