def maiores(lista,n):
    """Funcao que dada uma lista, retorna outra com todos os numeros da primeira maiores que N"""
    list.sort()
    indice = list.index(n)
    return lista[indice+1:]