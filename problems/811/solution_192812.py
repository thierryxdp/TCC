def colchao(medidas,H,L):
    """
    """
    medidas = list(sorted(medidas))
    if medidas[0] < H and medidas[1] < L: return "True"
    elif medidas[0] < H and medidas[2] < L : return "True" 
    elif medidas[1] < H and medidas[2] < L : return "True" 
    elif medidas[1] < H and medidas[0] < L : return "True" 
    elif medidas[2] < H and medidas[0] < L : return "True" 
    elif medidas[2] < H and medidas[1] < L : return "True"  
    else:
        return "False"