def faltante(lista):
    '''funcao que recebe uma lista de tamanho n-1 e retorna
    um numero inteiro x que faz parte do intervalo [1,n]
    mas nao pertence a lista
    lista-int'''
    proximo=0
    faltou=1
    while lista[proximo]==faltou:
        proximo=proximo + 1
        proximo<len(lista)
        faltou=faltou +1
    return faltou