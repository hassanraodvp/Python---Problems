# String to integer 
str = "123456"

print(str)
print(type(str))

int = int(str)
print(int)
print(type(int))


# String to float 
string = "123.456"

print(string)
print(type(string))

float_str = float(string)
print(float_str)
print(type(float_str))

# Float to Integer 
float_string = "123.456"

print(type(float_string))  # Output: <class 'str'>
print(float_string)  # Output: 123.456

# Convert float_string to float, then to int
float_int = int(float(float_string))
print(type(float_int))  # Output: <class 'int'>
print(float_int)


