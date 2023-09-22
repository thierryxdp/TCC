def colchao(medidas,H,L):
    '''Função que retorna True caso o colchão passe e False caso o colchão não consiga passar'''
    if H>L:
        return medidas[0]<=L and medidas[1]<=H
    else:
        return medidas[0]<=H and medidas[1]<=L