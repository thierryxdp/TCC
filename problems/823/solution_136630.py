def faltante(lPecas):
    '''Retorna qual peça n está faltando da lista de entrada de tamanho n-1;
       list -> int'''
    lPecas.sort()
    count=0
    pecaFaltando=1
    while count < len(lPecas):
        if pecaFaltando==lPecas[count]:
            pecaFaltando+=1
        count+=1
    return pecaFaltando