def filtra_pares(a,b,c,d):
    '''funçao que recebe uma tupla com 4 elementos e retorna apenas os seus elementos pares
    int,int,int,int->int,int'''
    return[n for n in tupla if n%2 ==0]
    tpl=(a,b,c,d)
    lst=filtra_pares(tpl)