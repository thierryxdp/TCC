import math
def bolos(a,b,c):
    ''' calcula a quantidade de bolo que João pode fazer, tendo como base o número de ingredientes '''
    farinha=a//2
    ovo=b//3
    leite=c//5
    return min (farinha,ovo,leite)