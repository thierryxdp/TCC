def intercala (lista1, lista2):
    '''Funçao que, dadas duas listas de tamanho 3, retorna uma terceira lista intercalando os elementos das listas 1 e 2'''
    ''' float -> float '''
    lista3 = []
    for i in range (0, len (lista1)):
        lista3.append (lista1 [i])
        lista3.append (lista2 [i])
    return lista3