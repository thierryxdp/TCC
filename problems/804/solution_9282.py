def filtra_pares(tupla):
    '''
    tupla(int,int,int,int)-> tupla'''
   	for numero in tupla:
        if numero%2 != 0:
            tupla.remove(numero)
    return tupla