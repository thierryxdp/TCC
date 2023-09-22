def soma_h(n):
    soma = 0
    for c in range(1, n + 1):
        inverso = (1/c)
        soma += inverso
    return round(soma, 2)


num = int(input('Digite um número: 2'))

print(soma_h(2))