#task 1

class Colors:
   PURPLE = "\033[0;35m"
n = int(input('Enter a number:'))
for i in range(n):
   s = '\033[0;35m*'
   print(s * n)


#task 2

x = int(input('Enter a number:'))
y = int(input('Enter another number:'))
for i in range(y):
    s = '*'
    print(s*x)


