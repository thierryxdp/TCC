def filtraMultiplos(lista,n):
    '''Retorna uma lista contendo os elementos da lista original que são divisíveis por n;
    list, int -> list'''
    i=0
    lista_div=[]
    while i<len(lista):
        if lista[i]%n==0:
            list.append(lista_div,lista[i])
        i=i+1
    return lista_div