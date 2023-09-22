"""Retorna uma lista ordenada crescente:
int,int->int"""
def maiores(inteiro,n):
    n=1
    listaF=[]
    for elemento in inteiro:
    	if elemento>n:
        	list.append(elemento,n)
    return inteiro[:n]