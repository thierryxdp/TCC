def filtraMultiplos(lista,n):
    ''' dado uma lista de números e um número n qualquer, retorna
    outra lista contendo todos os elementos da lista original divisíveis
    por n.
    list,int -> list'''
    lis = []
    i = 0
    while i < len(lista):
        listo = lista[i]
        i += 1
        if lista[i]%n == 0:
            lis = lis + listo
    return lis