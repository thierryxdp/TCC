def intercala(lista1, lista2):
    '''Função que recebe duas listas com três elementos
    e retorna uma terceira lista com os elementos das duas
    listas intercaladas
    [list], [list] -> [list]'''
    lista_3 = [lista1[0], lista2[0], lista1[1], lista2[1], lista1[2], lista2[2]]
    return lista_3