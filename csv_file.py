import csv
import re
import time

# 3. Создайте csv-файл с данными о ПК.
start = time.time()

with open('pc_info.txt') as file:
    text = file.read()

comp_list = [['Title', 'Spare']]

text = re.split('\n', text)

for i in text:
    index = i.find(':')
    comp_list.append([i[:index], i[index+1:].lstrip()])

#print(comp_list)

with open('pc_example.csv', 'w') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerows(comp_list)

print('Запись успешно выполнена - pc_example.cvs')

end = time.time() - start
print('Время выполнения операции: ' + str(end))