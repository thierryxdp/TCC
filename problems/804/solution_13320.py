def filtra_pares (list, pares):
    '''funcao que retorne os numeros pares'''
    list=[pares]
    lista1=[el for el in list if el %2 ==0]
    return lista1