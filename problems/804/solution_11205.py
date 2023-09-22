def filtra_pares(a):
    '''dado no parametro uma tupla com 4 elementos inteiros, retorna uma tupla com os elementos pares'''
    tupla_par = ()
    
    a1 = a[0]
    a2 = a[1]
    a3 = a[2]
    a4 = a[3]
    
    if (a1%2==0):
        tupla_par = tupla_par + (a1,)
    if (a2%2==0):
        tupla_par = tupla_par + (a2,)
    if (a3%2==0):
        tupla_par = tupla_par + (a3,)
    if (a4%2==0):
        tupla_par = tupla_par + (a4,)
    return tupla_par