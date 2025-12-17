def LerNotas():
    n = float(input("Digite uma nota: "))
    return n

def resultado(n1, n2):
    media = (n1 + n2) / 2
    print("Nota 1: ", n1)
    print("Nota 2: ", n2)
    print("Media: ", media,"Resultao: " ,end="")
    if media < 5:
        print("Reprovado")
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

A = LerNotas()
B = LerNotas()
resultado(A, B)