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
