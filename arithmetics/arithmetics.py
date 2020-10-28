a = input("Первое число - ")
b = input("Второе число - ")
op = input("Операция - ")

if op == '+':
	print(int(a) + int(b))
elif op == '-':
	print(int(a) - int(b))
elif op == '*':
	print(int(a) * int(b))
elif op == '/':
	if b != '0':
		print(int(a) / int(b))
	else:
		print("Неверные данные")
else: 
	print("Неизвестная операция")