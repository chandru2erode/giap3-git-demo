def sample():
    return "This is a sample python file."

def is_odd(num):
    return num % 2 != 0

print("Welcome Guys!!")
print(sample())

if is_odd(int(input('Enter a number: '))):
    print('The number is odd.')
else:
    print('The number is even.')