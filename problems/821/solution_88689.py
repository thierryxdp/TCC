def fatorial(n):
    """calcula o fatorial de um n número;
    int-> int"""
    
    fatorial = 1
    contador = 2
    while contador <= n:
        fatorial = fatorial*contador
        contador = contador + 1
    return n