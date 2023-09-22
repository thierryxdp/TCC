def faltante(lista):
    """ função que retorna um inteiro entre o intervalo [1,N] mas não está na lista de entrada
    list -> int"""
    i = 0
    while i <= len(lista):
        if i + 1 not in (lista):
            return i + 1 
        i = i + 1