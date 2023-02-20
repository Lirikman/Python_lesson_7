import json
import time
from doc_file import list_to_dict

# 4. Создайте json-файл с данными о ПК.

start = time.time()

comp_dict = list_to_dict()

comp_json = json.dumps(comp_dict)

with open('new_pc.json', 'w') as f:
    json.dump(comp_json, f)

print('Файл new_pc.json создан, информация о ПК успешно записана!')

end = time.time() - start

print('Время выполнения операции: ' + str(end))