text = 'Rigoberto Sanchez'

print(text[0:6:1])
print(text[7:])
print(text[:6])
print(text[::])
print(text[::-1])

text = 'Python'
print(text[0:4])

# es lo mismo que la linea de arriba ya que si no escribes nada por defecto es 0
print(text[:4])
print(text[2:])
print(text[::2])

text = "Hola mundo"
new_text = text[:5] + text[5:].replace('Mundo','Python')
print(new_text)

text = 'Python es genial'
parts = text.split()
parts2 = parts[:2]
print(parts)
print(parts2)
# siento que esto es repetitivo y poco util en la vida laboral
parts_reverse = parts[::-1]
print(parts_reverse)
text_reverse = ' '.join(parts_reverse)
print(text_reverse)

text = 'Python'
print(text[:2].lower() + text[2:].upper())

text = '   Hola tilin'
print(text.strip()[:5])
print(text.strip()[5:])