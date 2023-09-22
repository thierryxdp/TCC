def maiores(lista, n):
    """Função que retorna uma lista que contenha todos os numeros da lista original maiores que o numero 'N'.
    lista, int - > list"""
    
    list.append(lista,n)
    list.sort(lista)
    posicao=list.index(lista,n)+1
    return lista[posicao:]