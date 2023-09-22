def colchao(medidas,H,L):
    '''Recebe uma lista 'medidas com as dimensões dos colchões e os dados H e L do tamanho da porta pela qual ele terá de passar, retornando se é possível ou não transportar o colchão pela porta'''
    altura= medidas[0]
    largura= medidas[1]
    comprimento= medidas[2]
    if (altura<=H and largura<=L) or (altura<=H and comprimento<=L) or (comprimento<=H and largura<=L) or (comprimento<=L and largura<=H) or (comprimento<=H and largura<=L):
        return True
    else:
        return False