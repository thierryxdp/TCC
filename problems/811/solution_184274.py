def colchao(medidas, H, L):
    '''Função que diz se é possível passar um colchão que tem certas medidas
    (do menor para o maior) por uma porta com altura H e largura L. Retorna
    True caso seja possível e False caso não seja possível.'''
    if (medidas[2] <= H and medidas[0] <= L):
        return True
    elif (medidas[1] <= H and medidas[0] <= L):
        return True
    elif (medidas[2] <= H and medidas[1] <= L):
        return True
    else:
        return False