from decimal import Decimal, getcontext


age = 30
big_int = 1234567890987654321
decimal = 3.1415


print(age)
print(type(age))
print(big_int)
print(type(big_int))
print(decimal)
print(type(decimal))


number_complex= 2 + 3j
print(number_complex)
print(type(number_complex))

getcontext().prec = 10
num1 = Decimal('10.123456789')
num2 = Decimal('2.1')
result = num1 * num2
print(result)
print(type(num1))


numero = 42
numero_decimal = float(numero)
numerto_integral = int (3.1415)
print(numero_decimal)
print(numerto_integral)