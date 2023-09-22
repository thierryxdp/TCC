def filtra_pares (list):
    '''funcao que retorne os numeros pares'''
    list=[2,-16,7,9]
    lista1=[el for el in list if el %2 ==0]
    return lista1