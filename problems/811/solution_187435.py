def colchao(medidas,H,L):
    """funçao que, dados uma largura L de uma porta, uma altura H dessa mesma porta e as medidas A,B,C de um colchão (uma lista em ordem crescente dessas medidas), retorna um valor booleano True se e possivel passar o colchao pela porta ou False se nao for
    list(float,float,float),float,float--->bool"""
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    if (B<=L and C<=H)or(C<=L and B<=H)or(B<=L and A<=H)or(A<=L and C<=H)or(C<=L and A<=H)or(A<=H and B<=H):
        return True
    else:
        return False