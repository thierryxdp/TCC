def maiores(lista,n):
    """Função que dada uma lista e um Numero retorna outra lista que contenha todos os numeros maiores que Numero informado.
    parametros: lista,int-->lista"""
    if n not in lista:
        list.append(lista,n)
    list.sort(lista)
	indice = list.index(lista,n)
    fatiamento = lista[indice+1:]
    return fatiamento