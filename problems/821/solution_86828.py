from math import prod
def fatorial(x):
    '''Escreva um numero qualquer. A funcao retorna o fatorial
    desse numero.
    int -> int'''
    i=0
    fatorial=[]
    while x-1!=1:   #vai subtrair 1 de x ate chegar em 1
        fatorial=fatorial+[x-i]
        i=i+1
	return prod(fatorial)