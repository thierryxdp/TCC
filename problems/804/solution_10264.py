def par(x):
    '''retorna se um numero é par ou não
    int -> bool'''
    return x%2==0
def filtra_pares(a,b,c,d):
    '''filtra apenas os numeros pares dentre 
    4 numeros inteiros fornecidos;
    int,int,int,int -> tuple'''
    conjunto = a,b,c,d
    return filter(par,conjunto)