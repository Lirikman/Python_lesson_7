import re
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage
import time

# 1. Вручную создайте текстовый файл с данными (например, Характеристики ПК).
# 2. Создайте шаблон документа doc
# 3. Внесите данные из файла в шаблон2.

start = time.time()


def list_to_dict():
    with open('pc_info.txt') as file:
        text = file.read()
    title = []
    spare = []
    text = re.split('\n', text)
    for i in text:
        index = i.find(':')
        title.append(i[:index])
        spare.append(i[index + 1:].lstrip())
    new_dict = dict(zip(title, spare))
    return new_dict


# print(comp_dict)
if __name__ == "__main__":
    doc = DocxTemplate('pc.docx')

    img_size = Cm(15)
    pc = InlineImage(doc, 'pc.png', img_size)
    comp_dict = list_to_dict()
    comp_dict['pc'] = pc

    doc.render(comp_dict)
    doc.save('pc_new.docx')
    print('Шаблон успешно создан - pc_new.docx')

    end = time.time() - start
    print('Время выполнения операции: ' + str(end))
