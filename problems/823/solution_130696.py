def faltante(lista):
    """ dada uma lista com n numeros, descobre qual está faltando"""
    indice=1
    while indice in lista:
        indice= indice+1
    return indice