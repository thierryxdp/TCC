def filtra_pares(t):
    '''recebe uma tupla com quatro elementos inteiros como parâmetro
e retorna uma nova tupla contendo apenas os elementos pares da tupla 
original, na mesma ordem em que se encontravam'''
    if t[0]%2==0:
        p0=t[0]
    if t[1]%2==0:
        p1=t[1]
    if t[2]%2==0:
        p2=t[2]
    if t[3]%2==0:
        p3=t[3]
        return p0