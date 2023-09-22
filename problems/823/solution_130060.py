def faltante(lista):
    "função que dada uma lista, retorna qual número inteiro dessa lista está faltando.list->int."
    lista.sort()
    indice = 0
    while indice < len(lista):
        if indice+1 != lista[indice]:
            return indice+1
        indice = indice+1
    return len(lista)+1