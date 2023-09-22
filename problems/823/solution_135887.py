def faltante(lista):
    '''funcao que recebe uma lista de tamanho n-1 e retorna
    um numero inteiro x que faz parte do intervalo [1,n]
    mas nao pertence a lista
    lista-int'''
    proximo=0
    faltou=1
    while lista[proximo]==faltou:
        if proximo<len(lista):
            proximo=proximo + 1
            faltou=faltou +1
            elif proximo>len(lista):
                faltou= len(lista) + 1
    return faltou