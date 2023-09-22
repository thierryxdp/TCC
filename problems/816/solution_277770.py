def maiores (lista_int,n):
    """dada uma lista de inteiros e um inteiro 'n',retorna outra lista contendo todos os números da lista original maiores que 'n'"""
    list.append(lista_int,int(n))
    list.sort(lista_int)
    indice=list.index(lista_int,int(n))
    return lista_int[int(indice)+1:]