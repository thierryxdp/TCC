def maiores(lista,n):
    """Função que recebe uma lista e um numero inteiro e retorna todos os numeros da lista original maiores que n"""
    """lista, int->lista"""
    if n in lista:
        listamaior = sorted(lista)
        indexn=list.index(lista,n)
        return lista[(indexn+1):]
    else:
        list.append(lista,n)
        lista=sorted(lista)
        return lista[(indexn+1):]