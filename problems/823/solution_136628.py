def faltante(lPecas):
    '''Retorna qual peça n está faltando da lista de entrada de tamanho n-1;
       list -> int'''
    lPecas.sort()
    indice=0
    pecaFaltando=1
    while pecaFaltando == lPecas[indice]:
        pecaFaltando+=1
        indice+=1
    return pecaFaltando