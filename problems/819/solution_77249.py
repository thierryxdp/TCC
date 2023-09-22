def filtraMultiplos(lista,numero):
    '''retorna todos os numeros na lista que sao multiplos 
    do numero informado; list, int -> list'''
    i=0
    listaMultiplos=[]
    while i<len(lista):
        if lista[i]%numero==0:
            listaMultiplos = listaMultiplos+lista[i]
    return listaMultiplos