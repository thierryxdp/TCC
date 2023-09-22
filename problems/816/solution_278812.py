def maiores(lista_numero, n):
    """A funcao recebe uma lista de numeros inteiros e um numero n, e retorna outra lista com todos os numeros da lista original maiores que n.
    list, int -> list"""
    list.append(lista_numero,n)
    list.sort(lista_numero)
    ocorrencia=list.index(lista_numero,n)+1
    return lista_numero[ocorrencia:]