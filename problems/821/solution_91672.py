def fatorial(n):
    """Função que calcula o fatorial de um número n; int->int"""
    cont = 1
    fator = n
    while cont<n:
        fator*=cont
        cont+=1
    return fator