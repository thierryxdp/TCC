def faltante(lista):
    """Retorna qual número inteiro do intervalo [1,N] está faltando na lista.
    list->int"""
    n=0
    while n<len(lista):
        n=n+1
        if n not in lista:
            return n