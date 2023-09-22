def intercala(lista1, lista2):
    '''Funçao que recebe duas listas de tamanho 3 e retorna uma terceira lista com os elementos das duas primeiras intercalados (list, list -> list)'''
    l3 = [l1[0]] + [l2[0]] + [l1[1]] + [l2[1]] + [l1[2]] + [l2[2]]
    return l3