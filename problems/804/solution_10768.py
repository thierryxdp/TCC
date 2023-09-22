def par(x):
    '''retorna se um numero e par ou nao'''
    return x%2==0
def filtra_pares(n1,n2,n3,n4):
    '''retorna um conjunto com todos os
    numeros pares presentes no conjunto inicial;
    int,int,int,int -> tuple'''
    conjunto=(n1,n2,n3,n4)
    return filter(par,conjunto)