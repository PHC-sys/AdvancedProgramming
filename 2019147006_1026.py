import random
import string

ID_LENGTH = 8
MAIL_LENGTH = 5
NUMBER = 15
country = ["Korea", "Japan", "United Kingdom", "United States", "Canada"]
country_code = [".kr", ".jp", ".uk", ".us", ".ca"]

def email_generator(id_length, mail_length, number):
    partition = "@"
    ac = ".ac"
    univ_in_korea = ["snu", "yonsei", "korea"]
    country_code = [".kr", ".jp", ".uk", ".us", ".ca"]

    string_pool = string.ascii_letters
    digit_pool = string.digits
    letter_pool = string_pool + digit_pool

    email_address_list = []

    for n in range(number):
        email_address = ""
        for i in range(id_length):
            email_address += random.choice(letter_pool)

        email_address += partition

        if n < 3:
            email_address += univ_in_korea[n]

        else:
            for j in range(mail_length):
                email_address += random.choice(string_pool)

        email_address += ac

        s = n // 3
        code = country_code[s]
        email_address += code

        email_address_list.append(email_address)

    return email_address_list


results = email_generator(ID_LENGTH, MAIL_LENGTH, NUMBER)
random.shuffle(results)
print("Initial List: ", results, "\n")

email_address_dic = {}
s = 5
for i in range(s):
    email_address_dic[country[i]] = list()

for result in results:
    code = result[-3:]

    for i in range(s):
        if code == country_code[i]:
            email_address_dic[country[i]].append(result)

for i in email_address_dic:
    print(i, email_address_dic[i])
