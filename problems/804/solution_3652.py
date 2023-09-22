def filtra_pares(tupla):
    '''Função que recebe como entrada uma tupla de quatro elementos e retorna uma nova tupla contendo apenas os números pares da tupla de entrada; tuple->tuple'''
    x,y,z,w=tupla
    t=()
    if x%2==0:
        t=t+(x,)
    if y%2==0:
        t=t+(y,)
    if z%2==0:
        t=t+(z,)
    if w%2==0:
        t=t+(w,)
    if z%2==0:
        t=t+(z,)
    return t