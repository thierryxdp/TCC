def filtra_pares(a):
    '''dado uam tupla com quatro elementos inteiros, 
    retorna uma nova tupla contendo apenas elementos
    pares da tupla original.
    tuple --> tuple'''
    
    F=()
    w,x,y,z = a
    if w%2==0:
        F=F+(w,)
    if x%2==0:
        F=F+(x,)
    if y%2==0:
        F=F+(y,)
    if z%2==0:
        F=F+(z,)
        return F