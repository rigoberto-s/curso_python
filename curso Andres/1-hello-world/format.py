name = 'Rigoberto'

age = 20

text = f'Me llamo {name} y trngo {age} años'

print(text)

a = 5
b = 3

print(f"la suma de {a} + {b} es {a+b} ")


result = f'El precio es {a * b} dolares'
print(result)

price = 50

txt = f'Este producto es muy { 'caro' if price > 50 else 'Barato'}'
print(txt)

fruit = 'Manzanas'
txt = f'ME encantas las { fruit.upper()}'
print(txt)


price = 59
text = 'El precio es {price} dolares'
print(text.format(price = 59))

txt = "Oferta por solo {price:.2f} dolares"
print(txt.format(price = 60))