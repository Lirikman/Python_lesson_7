import re

from docxtpl import DocxTemplate

with open('pc_info.txt') as file:
    text = file.read()

title = []
spare = []

text = re.split('\n', text)

for i in text:
    index = i.find(':')
    title.append(i[:index])
    spare.append(i[index+1:].lstrip())

comp_dict = dict(zip(title, spare))

print(comp_dict)
doc = DocxTemplate('pc.docx')

doc.render(comp_dict)
doc.save('pc_new.docx')