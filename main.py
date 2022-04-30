
# Press the green button in the gutter to run the script.
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
from patterns import pattern_FIO, pattern_phone, pattern_phone_add, sub_pattern, sub_add_pattern
if __name__ == '__main__':


    with open("phonebook_raw.csv", encoding="utf8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    #pprint(contacts_list)

    # TODO 1: выполните пункты 1-3 ДЗ
    # ваш код

    new_contact_dict = {}
    for i,contact in enumerate(contacts_list):
        if i > 0:
            contact_full = ",".join(contact)
            #print(contact_full)
            result = re.findall(pattern_FIO, contact_full)
            #print(result)
            contact[0] = result[0]
            contact[1] = result[1]
            key = contact[0]+contact[1]
            if len (result) > 2:
                contact[2] = result[2]

            #organization = contact[3]
            #position = contact[4]


            phone = contact[5]
            phone = re.sub(pattern_phone, sub_pattern, phone) #замена основной части телефона
            phone = re.sub(pattern_phone_add, sub_add_pattern, phone) #замена доп части телефона
            contact[5] = phone

            #email = contact[6]

            if new_contact_dict.get(key):
                #если такой контакт уже существует, то объединяем информацию
                for i in range(2, 7) :
                    if new_contact_dict[key][i] == "":
                        new_contact_dict[key][i] = contact[i]
            else:
                #создаем новый контакт
                new_contact_dict.setdefault(key, contact)

    #print(new_contact_dict)
    new_contact_list = list(new_contact_dict.values())

    new_contact_list = [contacts_list[0]] + new_contact_list #добавляем заголовок csv
    pprint(new_contact_list)





    # TODO 2: сохраните получившиеся данные в другой файл
    # код для записи файла в формате CSV
    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        # Вместо contacts_list подставьте свой список
        datawriter.writerows(new_contact_list)