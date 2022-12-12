"""
2) Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
my_list = ['Весна Скоро\n', 'Лето не скоро\n', 'Осень прошла\n',
           'Зима идет сейчас\n']

with open("file_for_second_task.txt", "w", encoding="UTF-8") as file_object:
    file_object.writelines(my_list)

with open("file_for_second_task.txt", encoding="UTF-8") as file_object:
    LINES = 0
    for line in file_object:
        print(f'Число слов в строке ({LINES+1}): {len(line.split())}')
        LINES += 1
    print(f'Строк в файле: {LINES}')
