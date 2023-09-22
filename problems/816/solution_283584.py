def maiores(lista,n):
    """dada uma lista de números inteiros e um número n, retorne uma lista original com os números maiores que n em ordem crescente""""
    lista.append(n)
    list.sort(lista)
    a=int(lista.index(n))+1
    b=int(len(lista))
    return lista[a:b]