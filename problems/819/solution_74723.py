def filtraMultiplos(lista,n):
    ''' '''
    multiplos=[]
    contador=0
    while contador<len(lista):
        if lista[contador]%n==0:
            multiplos=multiplos+[lista[contador]]
        contador=contador+1
    return multiplos