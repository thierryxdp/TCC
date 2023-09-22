def soma_h(n):
    soma = 0
    lista = list(range(1,n+1))
    for i in lista:
        #fracao = 1/n
        soma = soma + 1/i
    return round(soma,2)