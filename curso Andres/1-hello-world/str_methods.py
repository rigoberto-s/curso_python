name = 'Andres Guzman'

course = 'Curso de python'

name_upper = name.upper()
print(name == name_upper)
print(name_upper)
print(course.lower())

print('-----------------------------------------')
word = 'curso de python de andres'
print(word.capitalize())
print(word.title())


txt = '     hola mundo     '
print(txt.strip())#para que es strip?
print(txt.lstrip())# esto elimina el espacio a la izquierda
print(txt.rstrip())

text = 'Hola java porfin'
print(text.replace('java','python'))

print('------------------------------------------------')
text = 'Andrez,Guzman,Jose,java'
data_list = text.split(",")#por que se puso un coma aqui
print(data_list[1])
print(data_list)

lista = ["Andrez", "Guzman", "Jose", "java"]
text = ' '.join(lista)#dejamos un espacio para que por cada palabra se deje un espacio
print(text)