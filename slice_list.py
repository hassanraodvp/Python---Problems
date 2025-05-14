name = ["John", "Doe", "Hazle", "Kaile", "Smith", "mark"]

print(name[:3])  # ['John', 'Doe', 'Hazle']
print(name[:4])  # ['John', 'Doe', 'Hazle', 'Kaile']

print(name[3:]) # ['Kaile', 'Smith', 'mark']
print(name[4:]) # ['Smith','mark']

print(name[::]) # ['John', 'Doe', 'Hazle', 'Kaile', 'Smith', 'mark']

print(name[0:3])  # ['John', 'Doe', 'Hazle']
print(name[0:4])  # ['John', 'Doe', 'Hazle', 'Kaile']
print(name[0:5])  # ['John', 'Doe', 'Hazle', 'Kaile', 'Smith']

print(name[1:3])  # ['Doe', 'Hazle']

print(name[2:5])  # ['Hazle', 'Kaile', 'Smith']

print(name[3:5])  # ['Kaile', 'Smith']

print(name[::2]) # ['John', 'Hazle', 'Smith']
print(name[::3])  # ['John', 'Kaile']
print(name[::4])  # ['John', 'Kaile']

print(name[::-1]) # ['mark', 'Smith', 'Kaile', 'Hazle', 'Doe', 'John']
print(name[::-2]) # ['mark', 'Kaile', 'Doe']