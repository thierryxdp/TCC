def faltante(lista):
    """função que retorna a peça faltando
    list->int"""
    n=0
    while n<len(lista)+1:
        if n in lista:
            n=n+1
        else:
            return n