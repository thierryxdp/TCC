"""Recebe uma lista de números e retorna os elementos que forem dividos por n:
int->int"""
def filtraMultiplos(n,num):
    n=[]
    l=0
    num=numero
    while l<len(numero):
        if numero[l]%n == 0:
            n= n + (numero[l],)
        l = l+1
    return n