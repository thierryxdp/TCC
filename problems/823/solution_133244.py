def faltante(lista):
    """Dada uma lista com N-1 inteiros numerados de 1 a N, descobre qual número
    inteiro desde intervalo está faltando; list->int"""
    list.sort(lista)
    contador=1
    while contador<len(lista):
        if lista[contador]!=lista[contador-1]+1:
            return lista[contador-1]+1
        contador=contador+1