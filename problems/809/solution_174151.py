def intercala(lista1, lista2):
    '''Faça uma função que dadas duas listas L1 e L2 de tamanho 3, gera uma lista L3 que ´e formada
intercalando os elementos de L1 e L2'''
   #str>str
    lista3=lista1[:]
    lista3.insert(1,lista2[0])
    lista3.insert(3,lista2[1])
    lista3.insert(5,lista2[2])
    return lista3