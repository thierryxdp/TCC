def maiores(lista, n):
    """Funcao que dada uma lista, retorna outra com todos os numeros da primeira maiores que N"""
    lista.sort()
    indice = lista.index(n)
    return lista[indice+1:]