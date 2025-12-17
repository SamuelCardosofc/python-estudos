qtd = 0
soma = 0
media = 0
valor = float(input("Digite um valor: "))

while valor > 0.0:
    soma += valor
    qtd += 1
    valor = float(input("Digite um valor: "))

media = soma / qtd
print("Total da soma: ", soma)
print("Quantidade de valores digitados: ", qtd)
print("Média dos valores: ", media)