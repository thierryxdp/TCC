def faltante(lista):
    """
    list->int
    :param lista: Recebe uma lista com numeros
    :param return: Retorna qual a peça faltante
    """
    n=1
    while n in lista:
        n = n + 1
        if n not in lista:
            return n 
    if n not in lista:
        return n