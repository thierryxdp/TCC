def fatorial(numero):
    """Calcula o fatorial de um número;
    int -> int"""
    lista = list(range(numero,0,-1))
    i=1
    c=1
    
    if numero == 1 or numero == 0:
        return 1
    
    while i < len(lista):
        produto= lista[i] * lista[i-1]
        c = produto*c
        i +=2
    return c