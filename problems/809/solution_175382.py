def intercala(lista1, lista2):
    '''função dada duas listas (L1 e L2) retorne uma nova lista (L3) intercalando os elementos de L1 e L2:
    int, int -> tupla'''
    return lista1[0:1]+lista2[0:1]+lista1[1:2]+lista2[1:2]+lista1[2:3]+lista2[2:3]