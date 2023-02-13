import json
import re
import time

# 4. Создайте json-файл с данными о ПК.

start = time.time()

with open('pc_info.txt') as file:
    text = file.read()

title = []
spare = []

text = re.split('\n', text)

for i in text:
    index = i.find(':')
    title.append(i[:index])
    spare.append(i[index + 1:].lstrip())

comp_dict = dict(zip(title, spare))

comp_json = json.dumps(comp_dict)

# print(type(comp_json), comp_json)

with open('new_pc.json', 'w') as f:
    json.dump(comp_json, f)

print('Файл new_pc.json создан, информация о ПК успешно записана!')

end = time.time() - start
print('Время выполнения операции: ' + str(end))
