def filtraMultiplos (lista,n):
    '''Função que recebe uma lista de numeros(lista) e um núm
    ero(n), e retorna outra lista contendo os elementos da li
    sta de entrada que são multiplo de n;list,int->list'''
    lista_resposta=[]
    proximo=0
    while lista_resposta<len(lista):
        if lista[proximo]%n==0:
            lista_resposta+=proximo
            proximo=proximo+1
    return lista_resposta