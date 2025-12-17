A = input("Digite o primeiro número: ")
B = input("Digite o segundo número: ")

if (A < B):
    aux = A;
    A = B;
    B = aux;
print("O maior valor é: ", A)
print("O menos valor é: ", B)