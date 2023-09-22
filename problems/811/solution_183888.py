def colchao(medidas,H,L):
    "a funcao calcula por meio de medidas, o colchao passe pela porta"
   
    if dimensoes[2]<=H and dimensoes[1]<=L:
        return True
    if dimensoes[1]<=H and dimensoes[0]<=L:
        return True
    if dimensoes[2]<=H and dimensoes[0]<=L:
        return True
    else:
        return False