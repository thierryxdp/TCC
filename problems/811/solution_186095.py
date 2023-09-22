def colchao(medidas,H,L):
    if (H>medidas[0] and H>=medidas[1]) or (H>medidas[0] and H>medidas[2]) or (H>medidas[2] and H>medidas[1]):
        if L>medidas[0] or L>medidas[1] or L>medidas[2]:
            return True
    if (L>medidas[0] and L>medidas[1]) or (L>medidas[0] and L>medidas[2]) or (L>medidas[2] and L>medidas[1]):
        if H>medidas[0] or H>medidas[1] or H>medidas[2]:
            return True    
    else:
        return False