def colchao(lista,H,L):
    '''função que reorna True ou False se as medidas do colchão
    são favoraveis para passar na porta. Em que recebe como parâmetro
    uma lista com as medidas do colchão em orddem crescente e H(altura)
    e L(largura).
    lista,int->bool. '''
    lista=[lista[0],lista[1],lista[2]]
    if min(lista)==lista[0] and lista[1]<lista[2] and lista[1]<=H:
        return True
    else:
        return False