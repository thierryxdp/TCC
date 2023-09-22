def filtraMultiplos (lista,numero):
    ''' A função retorna uma outra lista contendo todos
    os elementos da lista original que forem divisíveis
    por n
    list,int -> list'''
    divisiveis =[]
    proximo = 0
    while proximo <len(lista):
        if lista[proximo]%numero == 0:
            divisiveis = divisiveis + [lista[proximo],]
        proximo = proximo + 1 
    return divisiveis