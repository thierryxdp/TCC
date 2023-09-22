"""Recebe uma lista de números e retorna os elementos que forem dividos por n:
int->int"""
def filtraMultiplos(num,n):
    num=[]
    l=0
    while l<len(n):
     	if num[l]%n == 0:
            num= num + (n[l],)
    return n