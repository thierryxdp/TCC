def filtraMultiplos(lista,n):
    ''' Função que recebe como entrada uma lista de números e um número n. 
    retornando uma outra lista contendo todos os elementos da lista original divisíveis por n
    list, float -> list '''
    listaF = ()
    i = 0
    while i < len(lista):
        if int(lista[i])%n == 0:
            listaF = listaF + (lista[i],)
        i = i + 1
    return list(listaF)