def colchao(medidas,H,L):
    '''Função que dadas as dimensões de um colchão e a altura H e a largura L de uma porta, retorna se o colcão passa ou não pela porta. list,int,int -> bool'''
    area1 == A*B
    area2 == B*C
    area3 == C*A
    areaPorta == H*L
    if area1 < areaPorta:
        return True
    elif area2 < areaPorta:
        return True
    elif area3 < areaPorta:
        return True
    else:
        return False