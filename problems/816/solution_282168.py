"""Retorna uma lista ordenada crescente:
int,int->int"""
def maiores(inteiro,n):
    listaF=[]
    lista=list.append(inteiro,n)
    lista=list.sort(inteiro)
    for elemento in lista:
        if elemento >n:
            listaF.append(elemento,n)
    return listaF