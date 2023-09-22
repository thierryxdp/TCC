def filtraMultiplos(lista,n):
    '''verifica os multiplos de n presentes na lista dada;
    list,float->list'''
    lista1=[]
    x=0
    while x<len(lista):
        if lista[x]%n==0:
            list.append(lista1,lista[x])
        x=x+1
    return lista1