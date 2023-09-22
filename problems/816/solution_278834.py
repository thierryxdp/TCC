def maiores(lista,n):
    """Função que retorna uma lista com os numeros da lista original maiores que N"""
    lista.sort()
    indice = lista.index(n)
    return lista[indice+1:]