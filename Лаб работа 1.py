# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# 1 решение

import math
a = 3
b = 4
c = math.sqrt(b*b + a*a)
print(c)

# 2 решение

a = 179
print(a // 10 % 10)

# 3 решение

n = 10
n += 2 - n % 2
print(n)

# 4 решение

shortbreak = n //2
longbreak = n - shortbreak-1
time = n * 45 + shortbreak * 5 + longbreak * 15

hours = 9 + (time//60)
minutes = time % 60

print(str(hours) + " " + str(minutes))

# 5 решение

a = 40
b = 50

if a > b:
    print(a)
if a < b:
    print(b)
else:
    print(0)

# 6 решение

a = 7
b = 15
c = 4

if a>b>c:
    print(a)
if b>a>c:
    print(b)
else:
    print(c)

# 7 решение - не понял

# 8 решение

a = 3

b = 4

c = 5

if a + b > c and b + c > a and a + c > b:
    print('YES')
else:
    print('NO')

# 9 решение

a = 1

b = 2

c = 2

if a == b:
    print(a)
elif b == c:
    print(b)
elif c == a:
    print(c)
else:
    print(0)

# 10 решение

a = 1

b = 2

c = 1

if a > b:
    a, b = b , a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print(a , b , c)