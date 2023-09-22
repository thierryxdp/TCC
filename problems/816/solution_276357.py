def maiores(lista_numero , n):
    """Função que dada uma lista, de número inteiros e n , retorne outra lista que contenha o mesmo número da lista original """ 
    lista_numero.append(n)
    lista_numero.sort()

#    return list.sort(lista_de_numeros)
    return lista_numero