"""
4) Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться на
русские. Новый блок строк должен записываться в новый текстовый файл.
"""

with open("file_for_fourth_task_input.txt", 'r', encoding="UTF-8") as \
        file_object:
    result = []
    for line in file_object:
        string = line.split("—")
        if int(string[1]) == 1:
            string[0] = "Один"
        elif int(string[1]) == 2:
            string[0] = "Два"
        elif int(string[1]) == 3:
            string[0] = "Три"
        elif int(string[1]) == 4:
            string[0] = "Четыре"
        result.append(" —".join(string))
    print(result)

with open("file_for_fourth_task_output.txt", "w", encoding="UTF-8") as \
        file_object:
    file_object.writelines(result)
