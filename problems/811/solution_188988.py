def colchao(medidas,H,L):
    '''Função que dadas as dimensões de um colchão e a altura H e a largura L de uma porta, retorna se o colcão passa ou não pela porta. list,int,int -> bool'''
    len(medidas) == 3
    area1 == medidas[0]*medidas[1]
    area2 == medidas[1]*medidas[2]
    area3 == medidas[2]*medidas[0]
    areaPorta == H*L
    if area1 < areaPorta:
        return True
    elif area2 < areaPorta:
        return True
    elif area3 < areaPorta:
        return True
    else:
        return False