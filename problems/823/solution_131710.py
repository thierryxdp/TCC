def faltante(lista_num):
    """Recebe uma lista com N-1 números inteiros numerados de 1 a N e retorna
       o número faltante.
       list->int
       
       Parameters:
       lista_num: Uma lista com N-1 números inteiros numerados de 1 a N."""
    i=1
    while i-1<len(lista):
        if i not in lista:
            faltante=i
        i=i+1
    return faltante