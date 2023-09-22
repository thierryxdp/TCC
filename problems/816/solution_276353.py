def maiores(lista_de_numeros , n):
    """Função que dada uma lista, de número inteiros e n , retorne outra lista que contenha o mesmo número da lista original """ 
    lista_de_numeros.append(n)
    lista_de_numeros.sort()

#    return list.sort(lista_de_numeros)
    return lista_de_numeros