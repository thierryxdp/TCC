def colchao(medidas, h, l):
    """Funcao diz se Joao consegue passar seu colchao novo de altura: h e
    largura: l pela porta de sua casa que tem as dimensoes A x B x C dadas
    na lista: medidas, da menor para a maior medida """

    a = medidas[0]
    b = medidas[1]
    c = medidas[2]

    caso1 = a <= h and b <= l
    caso2 = b <= h and a <= l
    caso3 = b <= h and c <= l
    caso4 = c <= h and b <= l
    caso5 = a <= h and c <= l
    caso6 = c <= h and a <= l
    
    if caso1 or caso2 or caso3 or caso4 or caso5 or caso6:
        return True
    else:
        return False