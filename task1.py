"""
1) Создать программно файл в текстовом формате, записать в него построчно
данные, вводимые пользователем. Об окончании ввода данных свидетельствует
пустая строка.
"""
our_list = []
while True:
    user_string = input("Введите любую строку: ")
    if user_string == '':
        break
    new_string = user_string + '\n'
    our_list.append(new_string)

with open("file_for_first_task.txt", 'w', encoding="utf8") as file_object:
    file_object.writelines(our_list)

# Для просмотра того, что записалось
with open("file_for_first_task.txt", 'r', encoding="utf8") as file_object:
    content = file_object.readlines()
    print("Читаем из файла: ", content)
