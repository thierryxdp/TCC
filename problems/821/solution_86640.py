# Dado um inteiro n, esta função calcula n!
# int -> int
# OBS: Acrescentei uma mensagem de erro para o caso de n negativo.

def fatorial(n):
    fat = 1
    cont = 1
    
    if n==0:
        return fat
    elif (n<0):
        return 'Erro'
    else:
    	while cont<=n:
            fat = fat*cont
            cont = cont + 1
        return fat