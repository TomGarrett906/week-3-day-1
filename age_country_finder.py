import re
with open ('./user_records.txt') as f:
    data = f.read()
    # print(data)
    # for line in f:
    #     print(line)

a_pattern = re.compile('.+([0-9]{2})')
age_pattern = a_pattern.findall(data)
print(age_pattern)
#                         Age       Country
my_pattern = re.compile(r'(\d+), ([A-Z][A-Za-z ]+)')
age_country = my_pattern.findall(data)
print(age_country)
# print(f'Age: {age_pattern} Country: {country_pattern}')


def function(data, age_country, country_pattern):









# def age_countires(data, age_pattern, country_pattern):
#     valid_count = 0
#     invalid_count = 0
#     for line in data:
#         if (age_pattern, country_pattern) in line:
#             valid_count += 1           
#         else:
#             invalid_count += 1
#     return     


       







# print(f'AGE: {age_pattern}, Country: {country_pattern}')

