def filtra_pares(a,b,c,d):
    'Int,int,int->tup. Retorna, caso haja, os numeros pares da tupla de entrada na ordem em que foram dados.'
    return [n for n in (a,b,c,d) if n%2==0]