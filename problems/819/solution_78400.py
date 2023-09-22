def filtraMultiplos(lista,n):
    '''Função para filtrar os múltiplos de um número n. Tem como entrada uma lista de números e um número, e retorna outra lista contendo todos os elementos da lista original que
forem diviśıveis por n; list, int -> list'''
    ind=0
    num_elementos = len(lista)
    vazia=list()
    while (ind< num_elementos):
        if (lista[ind]%n==0):
            list.append(vazia,lista[ind])
        ind= ind +1
    return vazia