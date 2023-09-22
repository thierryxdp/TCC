def colchao(medidas,H,L):
    "a funcao calcula por meio de medidas, o colchao passe pela porta"
   
    if medidas[2]<=H and medidas[1]<=L:
        return True
    if medidas[1]<=H and medidas[0]<=L:
        return True
    if medidas[2]<=H and medidas[0]<=L:
        return True
    else:
        return False