def fatorial(numero):
    """ Dado o valor de entrada, retorna o valor fatorial dele;
        int -> int"""
    
    ultimon = numero + 1
    lista = list(range(1, ultimon))
    fatorial = 1
    i = 0
    while i < len(lista):
        fatorial = fatorial *lista[i]
        i += 1
    return fatorial