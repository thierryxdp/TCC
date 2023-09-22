""" Recebe uma tupla com 4 elementos inteiros como argumento,
e retorne uma nova tupla contendo apenas os elelementos pares da tupla
original, na mesma ordem em que se encontravam.
Assinatura: tuple --> tuple(...)
Testes:
filtra_pares((2,2,2,2)) == (2, 2, 2, 2)
filtra_pares((1,2,2,2)) == (2, 2, 2)
filtra_pares((2,2,1,2)) == (2, 2, 2)
filtra_pares((2,2,2,1)) == (2, 2, 2) 
"""
def resto(a, b):
    return a % b

def eh_par(n):
    return resto(n, 2) == 0

def filtra_pares(t):
    ret = ()
	if eh_par(t[0]):
        ret = ret + (t[0], )
    if eh_par(t[1]):
    	ret = ret + (t[1], )
    if eh_par(t[2]):
        ret = ret + (t[2], )
    if eh_par(t[3]):
        ret = ret + (t[3], )
    return ret