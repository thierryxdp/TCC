import numpy as np
def filtraMultiplos(lista,n):
    '''função que que filtra os multiplos de n da lista, list,int->list'''
    i=0
    multiplos=[]
    while i<len(lista):
        if lista[i]% np.icm(lista[i],n)==0:
            multiplos=multiplos+lista[i]
        i=i+1
    return multiplos