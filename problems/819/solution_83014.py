def filtraMultiplos(lista,numero):
    '''
	função que recebe uma lista de números e um número e retorna outra lista contendo todos os elementos da lista original que forem divisíveis por n;
    list, int -> list
    '''
	i = 0
    lista_nova = []
    while i < len(lista):
        if lista[i] % numero == 0:
            lista_nova = lista_nova + lista[i]
        i = i + 1
    return lista_nova