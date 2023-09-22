def colchao(medidas,H,L):
    '''Fução que retorna se é possível ou não passar com 
    um colchão por uma porta, dada'''
    
    dimensoes=str(medidas)
    dimensoes=str.split(dimensoes)
    B=int(str.strip(dimensoes[1],','))
    C=int(str.strip(dimensoes[2],']'))
    
    if (B<=H or C<=L):
        return True
    else:
        return False