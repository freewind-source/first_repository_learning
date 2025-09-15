print ("Добро пожаловать в калькулятор чаевых!")
print ("by Brian Moser")
bill = input("Какова общая сумма счёта?: ")
tip_percent = input ("Сколько процентов чаевых вы можете оставить ^_^: ")
bill_amount = float(bill)
tip_amount = float(tip_percent)
calc = bill_amount * tip_amount / 100
calc2 = bill_amount + calc
print (f"\nСумма чаевых: {round(calc, 2)} руб.")
print (f"Итоговая сумма к оплате: {round(calc2, 2)} руб.")