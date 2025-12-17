arquivo = open("estudo/arqTEXT.txt", "w")

arquivo.write("Curso Python \n")
arquivo.write("Aula Prática \n")
arquivo.close()

leitura = open("estudo/arqTEXT.txt", "r")
print(leitura.read())
leitura.close()