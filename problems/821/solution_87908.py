def fatorial(n):
    i = 1
    resposta = 0
    while (n-i) != 0:
        resposta = n*(n-i)
        i = i+1
    return resposta