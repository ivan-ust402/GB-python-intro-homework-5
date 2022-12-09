"""
3) Создать текстовый файл (не программно), построчно записать фамилии
сотрудников и величину их окладов (не менее 10 строк). Определить, кто из
сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""
employee = {"Петров": 20000, "Иванов": 30000, "Сидоров": 10000,
            "Николаев": 50000, "Степанов": 70000, "Коробкин": 11000,
            "Воронов": 15000, "Синицын": 17000, "Рябов": 22000, "Сизов": 32000,
            "Галкин": 19000}

with open("file_for_third_task.txt", "w", encoding="UTF-8") as file_object:
    for surname, salary in employee.items():
        file_object.write(f'{surname}: {salary}\n')

with open("file_for_third_task.txt", "r", encoding="UTF-8") as file_object:
    found_persons = []
    SUM_SALARY = 0
    COUNT_OF_PERSONS = 0
    for line in file_object:
        common_list = line.split(':')
        if int(common_list[1]) < 20000:
            print(f'Оклад меньше 20000: {common_list[0]}')
        COUNT_OF_PERSONS += 1
        SUM_SALARY += int(common_list[1])
    avarage_salary = SUM_SALARY / COUNT_OF_PERSONS

    print(f'Средний доход сотрудников: {avarage_salary}')
