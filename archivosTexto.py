from io import open



''' archivo1 = open('archivo.txt','a')
archivo1.write("\n Saludo IDGS801 nuevo")
archivo1.close() '''


''' archivo1 = open('archivo.txt','r')
print(archivo1.read())
archivo1.seek(0)
print(archivo1.read())
archivo1.close() '''

archivo1 = open('archivo.txt','r')
# print(archivo1.readlines())
for datos in archivo1.readlines():
    print(datos.rstrip())

