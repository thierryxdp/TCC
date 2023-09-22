def filtraMultiplos(lista,n):
    '''Funcao que retorna uma lista com os multiplos de n list,int->list'''
    multiplos=[]
    x=0
    while x<len(lista):
        if lista[x]%n==0:
            multiplos=multiplos+[lista[x]]
            x=x+1
    return multiplos