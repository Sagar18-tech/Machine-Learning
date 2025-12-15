
text="name: sagar, age: 22, city: Belagavi,pin: 590016"
#text=input("Enter the data in key value format \n")
x=text.strip()
pairs=x.split(',')
data={}
for pair in pairs:
    key,value=pair.split(':')
    key=key.strip().replace("'", '')
    value=value.strip().replace("'", '')
    if value.isdigit():
        value = int(value)
    data[key]=value
print(data)

# Output: {'name': 'sagar', 'age': 22, 'city': 'Belagavi'}