"""Recebe uma lista de números e retorna os elementos que forem dividos por n:
int->int"""
def filtraMultiplos(n,num):
    n=[]
    l=0
    while l<len(n):
     	if num[l]%n == 0:
            n= n + (num[l],)
        l= l+1
    return n