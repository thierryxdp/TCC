def maiores(lista,n):
    """Função que recebe uma lista e um numero inteiro e retorna todos os numeros da lista original maiores que n"""
    """lista, int->lista"""
    listamaior=list.append(lista,n)
    sorted(listamaior)
    x=list.index(listamaior,n)
    return listamaior[x+1:]