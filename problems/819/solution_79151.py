def filtraMultiplos(lista,numero):
    '''dado uma lista de numeros(lista) e um numero(numero), retorna outra lista contendo todos os elementos da lista original que forem divisiveis por (numero); list,float -> list'''
    indice = 0
    lista2 = []
    while indice < len(lista):
        if lista[indice]%numero == 0:
            lista2 = lista2 + [lista[indice],]
        indice = indice + 1
    return lista2