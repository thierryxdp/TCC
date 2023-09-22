def filtra_pares(tupla):
    '''retorna uma nova tupla com os elementos pares de uma tupla com 4 elementos inteiros de entrada
    tup -> tup'''
    if (tupla[0])%2==0:
         a = (tupla[0],)
    else: 
         a = ()
    if (tupla[1])%2==0:
         b = (tupla[1],)
    if (tupla[2])%2==0:
         c = (tupla[2],)        
    if (tupla[3])%2==0:
         d = (tupla[3],)
    return a+b+c+d