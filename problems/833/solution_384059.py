def conta_numero(numero,matriz):
    """conta quantas vezes um numero x aparece em uma matriz;
    int, matriz, -> int"""
    
    m = matriz
    n = numero
    c = 0

    return (len(matriz)).count(n)