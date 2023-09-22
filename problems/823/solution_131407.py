def faltante (lista_faltando):
    """dada uma lista com N − 1 inteiros numerados de 1 a N, 
    descobre qual número inteiro deste intervalo está faltando. list->int"""
    list.sort(lista_faltando)
    indice = 0
    while indice < len(lista_faltando) and lista_faltando[indice] == indice+1:
        indice += 1
    return indice+1