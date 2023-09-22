def colchao(medidas,H,L):
    '''Fução que retorna se é possível ou não passar com 
    um colchão por uma porta, dadas medidas=uma lista com
    as medidas do colchão (A,B,C) onde A=largura B=comprimento
    C=altura, H= altura da porta e L=largura da porta.
    list,int,int->bool'''
    
    dimensoes=str(medidas)
    dimensoes=str.split(dimensoes)
    B=int(str.strip(dimensoes[1],','))
    C=int(str.strip(dimensoes[2],']'))
    
    if (B<=H or C<=L):
        return True
    else:
        return False