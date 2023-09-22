def fatorial(m):
    "funcao que dado um fatorial, calcula o fatorial desse numero"
    i = 1
    fatorial = 1
    while i <= m:
        fatorial = fatorial * i
        i = i + 1
        return fatorial