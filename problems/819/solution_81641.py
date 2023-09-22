"""Recebe uma lista de números e retorna os elementos que forem dividos por n:
int->int"""
def filtraMultiplos(n):
    lista = ()
    l = 0
    while l < len(n):
     	if n[l]%n == 0:
            lista= lista + (n[l],)
   		l = l+ 1
    return lista