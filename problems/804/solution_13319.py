def filtra_pares (list, num):
    '''funcao que retorne os numeros pares'''
    list=[num]
    lista1=[el for el in list if el %2 ==0]
    return lista1