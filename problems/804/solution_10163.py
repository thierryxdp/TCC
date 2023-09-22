def par(x):
    '''define se um numero e par ou nao'''
    return x%2==0
def filtra_pares(a,b,c,d):
    '''retorna um conjunto com todos os 
    numeros pares presentes no conjunto inicial;
    int,int,int,int -> tuple'''
    return filter(par,filtra_pares)