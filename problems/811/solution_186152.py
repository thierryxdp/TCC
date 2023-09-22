def colchao(medidas,H,L):
    '''Recebe uma lista 'medidas com as dimensões dos colchões e os dados H e L do tamanho da porta pela qual ele terá de passar, retornando se é possível ou não transportar o colchão pela porta'''
    altura= medidas[0]
    largura= medidas[1]
    comprimento= medidas[2]
    if (altura<=H and comprimento<=L):
        return True
    if (comprimento<=H and largura<=L):
        return True
    if (largura<=H and comprimento<=L):
        return True
    if (altura<=H and largura<=L):
        return True
    if (comprimento<=H and altura<=L):
        return True
    if (largura<=H and altura<=L):
        return True
    else:
        return False