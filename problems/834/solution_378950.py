def media_matriz(matriz):
    '''Esta e a funcao que calcula a media
de todos os n termos de uma matriz qualquer'''
    cont=0
    for linha in matriz:
        cont=sum(linha)
    return cont/len(matriz)