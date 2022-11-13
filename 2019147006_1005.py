import random
import string
import pandas as pd

file_name = 'email_address_list'

ID_LENGTH = 8
MAIL_LENGTH = 5
NUMBER = 10


def email_generator(id_length, mail_length, number):
    partition = "@"
    com = "gmail.com"

    string_pool = string.ascii_letters
    digit_pool = string.digits
    letter_pool = string_pool + digit_pool

    email_address_list = []

    for n in range(number):
        email_address = ""
        for i in range(id_length):
            email_address += random.choice(letter_pool)

        email_address += partition
        '''
        for j in range(mail_length):
            email_address += random.choice(string_pool)
        '''
        email_address += com

        email_address_list.append(email_address)

    return email_address_list


results = email_generator(ID_LENGTH, MAIL_LENGTH, NUMBER)
index = [i+1 for i in range(len(results))]

df_write_csv = pd.DataFrame({file_name: results}, index= index)
df_write_csv.to_csv(file_name)

df_read_csv = pd.read_csv(file_name, index_col=0)

print(df_read_csv)
