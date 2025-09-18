print ("Простой калькулятор v.0.1 by Brian Moser")
first = int(input ("Введите первое число: "))
second = int(input ("Введите второе число: "))
print ("Для справки, в данной версии доступны: сложение(+), вычитание(-), умножение(*), деление(/), возведение в степень (**)")
type = input("Выберите тип математической операции: ")
if type == "+":
    print (first + second)
elif type == "-":
    print (first - second)
elif type == "*":
    print (first * second)
elif type == "/":
    print (first / second)
elif type == "**":
    print (first ** second)
else:
    print ("Неверное значение!")
input ("Нажмите Enter для завершения!")
