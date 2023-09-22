def colchao(medidas,H,L):
    " " "Descobre se um colchão passa por uma porta, dadas a medidas do colçhão(medidas(A,B,C)),altura da porta(H) e largura da porta(L);lista, int, int, -> boolean " " " 
    if (medidas[1]<L and medidas[0]<H) or (medidas[0]<L and medidas[1]<H):
        return True
    elif (medidas[0]<L and medidas[2]<H) or (medidas[2]<L and medidas[0]<H):
        return True
    elif (medidas[1]<L and medidas[2]<H) or (medidas[2]<L and medidas[1]<H):
        return True
    else:
        return False