from pprint import pprint
import csv
import re


def match_names(contacts_list):
  for element in contacts_list:
    text = element[0] + ' ' + element[1] + ' ' + element[2]
    pattern = '\s+'
    lastname, firstname, surname = re.split(pattern,text,maxsplit=2,flags=0)
    sub_pattern = '\w+'
    element[0], element[1], element[2] = lastname, firstname, surname.rstrip()
  return contacts_list

def edit_phones(contacts_list):
  for element in contacts_list:
    text = element[5]
    pattern = '^(\+7|8)\s?\(?(\d{3})\)?[-|\s]?(\d{3})?[-|\s]?(\d{2})?[-|\s]?(\d{2})(\s([|(]?(доб.)\s?((\d+))[|)]*))?'
    sub_pattern = r'+7(\2)\3-\4-\5 \8\9'
    result = re.match(pattern, text)
    res = re.sub(pattern, sub_pattern, text, re.I)
    element[5] = res.rstrip()
  return contacts_list

def merge(contacts_list,tag=2):
  newlist = []
  for element in contacts_list:
    newlist.append(element)
  for element in contacts_list:
    for i in newlist:
      if element == i:
        pass
      elif len(list(set(element) & set(i))) > tag:
        for j in range(len(element)):
          if i[j] == '':
            i[j] = element[j]
        del newlist[newlist.index(element)]
  return newlist


if __name__ == '__main__':
  # читаем адресную книгу в формате CSV в список contacts_list
  with open('phonebook_raw.csv',encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=',')
    contacts_list = list(rows)
    
  # TODO 1: выполните пункты 1-3 ДЗ
  match_names(contacts_list)
  edit_phones(contacts_list)
  contacts_list = merge(contacts_list)

  # TODO 2: сохраните получившиеся данные в другой файл
  # код для записи файла в формате CSV
  with open('phonebook.csv', 'w', encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)