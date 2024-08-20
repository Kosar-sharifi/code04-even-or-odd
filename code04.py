num = int(input('enter number = '))
if num % 2 == 0:
    if num % 5 == 0:
        num2 = float(input('enter number2 = '))
        num3 = num + num2
        print('num3 = ' , num3)
    else:
        ('prin number dose not % 5 = 0')
else:
    print('number is Odd')