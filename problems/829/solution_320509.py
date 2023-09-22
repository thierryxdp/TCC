def soma_h(n):
    soma = 0
    lista = list(range(n+1))
    for i in lista:
        soma = soma + (1/n)
    round(soma,2)
    return soma