def filtra_pares(a,b,c,d):
    '''funçao que recebe uma tupla com 4 elementos e retorna apenas os seus elementos pares
    int,int,int,int->int,int'''
    return[filtra_pares(a,b,c,d) for filtra_pares(a,b,c,d) in tupla if n%2 ==0]