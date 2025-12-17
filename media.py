notaA = float(input("Digite a primeira nota: "))
notaB = float(input("Digite a segunda nota: "))

media = (notaA + notaB) / 2

if media >= 7.0:
    print("A média: %.1f - Aprovado"% media)
else:
    print("A média: %.1f - Reprovado"% media)