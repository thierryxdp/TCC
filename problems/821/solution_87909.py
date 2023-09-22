def fatorial(n):
    i = 1
    resposta = n
    while (n-i) != 0:
        resposta = n*(n-i)
        i = i+1
    return resposta