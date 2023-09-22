"""Recebe uma lista de números e retorna os elementos que forem dividos por n:
int->int"""
def filtraMultiplos(num,n):
    lista = ()
    l = 0
    while l < len(n):
     	if n[l]%n == 0:
            num= num + (n[l],)
    return n