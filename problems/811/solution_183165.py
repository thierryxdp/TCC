def colchao(medidas,H,L):
    '''função que dado as medidas de um colção retorna  True se essas
    medidas é menor ou igual do que a altura e largura de um determinada porta,
    se não retorna False
    list -> bool'''
    if L >= medidas[0] and H >= medidas[1] or H >= medidas[0] and L >= medidas[1]:
        return True
    else:
        return False