def filtraMultiplos(lista,n):
    '''função que retorna lista com números 
       multiplos do numero n, dados lista e o número n;
       list, int => list'''
    final = []
    i=0
    while i < len(lista):
        if lista[i] % n == 0:
            final = final+[lista[i],]
            i=i+1
    return final