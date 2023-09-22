def intercala(lista1,lista2):
    '''recebe duas tuplas de três elementos cada(lista1 e lista2) e retorna uma tupla de seis elementos intercalando as duas tuplas.'''
    return lista1[:1] +lista2[:1]+lista1[1:2:]+lista2[1:2:]+lista1[2:3:]+lista2[2:3:]