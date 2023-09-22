def filtraMultiplos(lista,numero):
    """fução que recebe uma lista com numeros e um numero então retorna outra lista com os muultiplos daquele numero que estão na lista
    list,int->list"""
    n=0
    multiplos=[]
    while n<len(lista):
        if lista[n]/numero == int:
            list.append(multiplos,lista[n])
            n=n+1
        else:
            n=n+1
    return multiplos