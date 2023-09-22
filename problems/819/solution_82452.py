def filtraMultiplos(lista,numero):
    ''' funçao que rece uma lista e um numero n, e filtra os multiplos do numero n.
list,int -> list'''
    indice=len(lista)
    contador=0
    list_mult=[]
    while contador < indice:
        if lista[contador]%numero==0:
            list_mult+=[lista[contador],]
        contador+=1
    return list_mult