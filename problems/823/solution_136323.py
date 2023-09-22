def faltante(lista):
    '''funcao que recebe uma lista de tamanho n-1 e retorna
    um numero inteiro x que faz parte do intervalo [1,n]
    mas nao pertence a lista
    lista-int'''
    proximo=0
    proximo2=0
    faltou=1
    while proximo2<len(lista):
        while lista[proximo]==faltou:
            proximo=proximo + 1
            faltou=faltou +1
        proximo2= proximo2 + 2
    return faltou