def maiores(lista_numero,n):
    """Dada uma lista de numeros inteiros e um numero inteiro n, retorna outra lista, que contem todos os numeros da lista original maiores que n, ordenados em ordem crescente.. str -> str"""
    lista_numero.append(n)
    list.sort(lista_numero)
    x=lista_numero.index(n)
    del(lista_numero[:x+1])
    return lista_numero