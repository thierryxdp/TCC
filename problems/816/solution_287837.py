def maiores(lista_numero,n):
    '''funcao que dada uma lista, retorna todos os numeros maiores que n da lista original'''
    lista_numero.append(n)
    list.sort(lista_numero)
    x=lista_numero.index(n)
    del(lista_numero[:x+1])
    return lista_numero