def soma_h(n):
    lista = list(range(1,n))
    soma = 0
    for i in lista:
        soma = soma + 1/i
    a = round(soma,2)
    return a