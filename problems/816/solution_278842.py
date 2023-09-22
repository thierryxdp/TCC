def maiores(lista, n):
    """Funcao que dada uma lista, retorna outra com todos os numeros da primeira maiores que N"""
    lista.sort(lista)
    indice = lista.index(lista, n)
    return lista[indice+1:]