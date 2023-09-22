"""Recebe uma lista de números e retorna os elementos que forem dividos por n:
int->int"""
def filtraMultiplos(num,n):
    lista = ()
    l = 0
    while l < len(num):
     	if num[l]%n == 0:
            lista= lista + (num[n],)
   			l = l+ 1
    return n