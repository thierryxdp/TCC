def filtraMultiplos(lista,n):
    """analisa se todos os numeros da lista são multiplos de n;
    lista, int -> lista"""
    resultado= []
    repetiçao = 0
    while repetiçao < len(lista):
        if lista[repetiçao]%n =0:
            resultado = resultado + [lista[repetiçao]]
            repetiçao = repetiçao + 1
        else:
            repetiçao = repetiçao + 1
    return resultado