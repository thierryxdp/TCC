"""Retorna uma lista ordenada crescente:
int,int->int"""
def maiores(inteiro,n):
    listaF=[]
    lista=list.append(inteiro,n)
    lista=list.sort(inteiro)
    for inteiro in lista:
        if inteiro >n:
            listaF.append(inteiro,n)
    return listaF