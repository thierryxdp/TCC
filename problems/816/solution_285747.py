def maiores(lista,n):
    '''Retorna uma nova lista que contem todos os números da lista original maiores 
    que n, em ordem crescente.'''
    n_lista = [n]
    lista_nova = lista + n_lista
    list.sort(lista_nova)
    indice = list.index(lista_nova,n)
    
    return lista_nova[indice+1:]