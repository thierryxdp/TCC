def intercala(lista1, lista2):
    '''funcao que recebe duas listas l1 e l2, gerando uma
       nova lista(l3) que intercala os elementos de l1 e l2
       list, list -> list'''
    return lista1[0:1]+lista2[0:1]+lista1[1:2]+lista2[1:2]+lista1[2:]+lista2[2:]