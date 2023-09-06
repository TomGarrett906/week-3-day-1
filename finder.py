import re
with open ('./user_records.txt') as f:
    data = f.readlines()
    # print(data)

# pattern = re.compile('([0-9]{2}), ([A-Z][A-Za-z ]+)')
pattern = re.compile('([\d]{2}), (\w][\w ]+)')

valid_count = 0
invalid_count = 0

for d in data:
    match = pattern.search(d)
    if match:
            age = match.group(1)
            country = match.group(2)
            print(f"Age: {age}\nCountry: {country}\n")
            valid_count += 1
    else:
            # print('Invalid Entry')
            invalid_count += 1
       
print("Valid Record: " + str(valid_count))
print("\nInvalid Record: " + str(invalid_count) + "\n")


