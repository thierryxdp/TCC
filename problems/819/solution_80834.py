def filtraMultiplos (multiplos,n):
    '''recebe a lista multiplos e um numero n e retorna uma
    nova lista com os elementos de multiplos que forem	
    divisiveis por n
    list,float->list'''
    acum=[]
    cont=0
    while cont<len(multiplos):
        x=multiplos[cont] % n
        if x==0:
            acum=acum+multiplos[cont]
        cont=cont+1
    return acum