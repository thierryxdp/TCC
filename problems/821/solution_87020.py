def fatorial(n):
    """Funcao que calcula o fatorial de um numero n . Int--> Int """
    fatorial = 1
    count = 1
    
    while count <= n:
        fatorial = fatorial * count
        count += 1
    return fatorial