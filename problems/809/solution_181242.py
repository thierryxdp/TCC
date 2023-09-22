def intercala(lista1, lista2):
    '''Funcao que faz chamada definida por duas lista L1 e L2 de tamanho 3 e com isso
    gera uma lista L3'''
    return lista1[ :1]+lista2[ :1]+lista1[1:2]+lista2[1:2]+lista1[2:3]+lista2[2:3]