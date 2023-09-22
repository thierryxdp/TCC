def filtraMultiplos(lista,n):
    ''' Essa função recebe uma lista de números e um número n, e retorna outra lista com todos os números da primeira que forem divisíveis por n;
    list, int -> list. '''
    i=0
    nova_lista=list()
    while i < len(lista):
        mtp= lista[i]%n
        if mtp == 0:
            list.append(nova_lista,lista[i])
        i=i+1
    return nova_lista