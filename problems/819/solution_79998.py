def  filtraMultiplos ( lista , n ):
    '''filtra os multiplos de um número n, recebendo como entrada uma lista de numeros e o numero e retorna outra lista contendo todos os elementos da lista original que principais divisiveis por n'''
    '''list, float -> list'''
    lista1 = ()
    i = 0
    while i < len(lista):
        if int(lista[i]) % n == 0:
            lista1 = lista1 + (lista[i],)
            i = i + 1
    return lista1