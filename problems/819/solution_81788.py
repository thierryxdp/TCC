def filtraMultiplos(lista,n):
    '''recebe uma lista de números e um número n e retorna outra lista contendo os elementos da lista original divisíveis por n; list,int->list'''

    resultado = []
    
    for i in range(0,len(lista)):
        if lista[i]/n == lista[i]//n:
            list.append(resultado,lista[i])
    return resultado