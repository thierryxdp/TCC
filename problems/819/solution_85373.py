def filtraMultiplos(lista,n):
    '''a'''
    tot=len(lista)
    cont=0
    multiplos=[]
    while tot>cont:
        if lista[cont]%n==0:
            multiplos.append(lista[cont])
        cont=cont+1
    return multiplos