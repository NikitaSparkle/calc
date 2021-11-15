print('First num')
num1 = input()

print('Second num')
num2 = input()

print('Action')
action = input()

if action == '/':
    if num2 == '0':
        print('error')
    else:
        print(int(num1) / int(num2))

elif action == '+':
    print(int(num1) + int(num2))

if action == '*':
    print(int(num1) * int(num2))
else:
    print('error')

if action == '^':
    print(int(num1)**int(num2))
else:
    print('error')

if action == '!':
    num3 = 1
    result = 1
    while(int(num3)<=int(num1)):
        result = int(result) * int(num3)
        num3 = int(num3) + 1
    print(result)
else:
    print('error')