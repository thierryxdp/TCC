def par(n):
    '''retorna o numero se for par'''
    if n%2==0:
        return n

def filtra_pares(a,b,c,d):
    '''retorna uma tupla com os numeros pares de entrada
    int,int,int-->tupla'''
    x=a,b,c,d
    list(filter(par,x))