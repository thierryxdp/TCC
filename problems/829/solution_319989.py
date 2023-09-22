def soma_h(n):
    lista = list(range(1,(n+1)))
    soma = 0
    for i in lista:
        soma = soma + 1/i
    return soma