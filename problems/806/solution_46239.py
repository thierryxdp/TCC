def colisao(tup1,tup2):
    '''Recebe duas tuplas com quatro valores inteiros cada uma,
    representando as coordenadas do primeiro retângulo e do segundo.
    Retorna se os retângulos colidem ou não.
    tuple,tuple -> bool'''
    #A melhor forma de entender essa questão é fazer um desenho
    #e investigar os casos em que NÃO ocorre uma colisão.
    #Filtrados esses, todos os outros são colisões.
    if tup2[0] > tup1[2] or tup2[2] < tup1[0] or tup1[3] < tup2[1] or tup1[1] > tup2[3]:
        return False
    else:
        return True