def fatorial(n):
    i = 1
    resposta = 0
    while (n-i) != 0:
        i = i+1
        resposta = n*(n-i)
    return resposta