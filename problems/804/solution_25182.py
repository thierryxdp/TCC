def filtra_pares(pares):
    '''
função que retorna os numeros pares
de uma tupla 
'''
a = ()
if pares[0] % 2 == 0:
    a = a + (pares[0],)
else:
    a = a
if pares[1] % 2 == 0:
    a = a + (pares[1],)
else:
    a = a
if pares[2] % 2 == 0:
    a = a + (pares[2],)
else:
    a = a
if pares[3] % 2 == 0:
    a = a + (pares[3],)
else:
    a = a
return a