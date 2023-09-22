def colchao(medidas,H,L):
    ''''''
    if (medidas[0]<=L and medidas[1]<=H) or (medidas[0]<=H and medidas[1]<=L) or (medidas[1]<=H and medidas[2]<=L) or (medidas[1]<=L and medidas[2]<=H) or (medidas[0]<=H and medidas[2]<=L) or (medidas[0]<=L and medidas[2]<=L):
        return True
    else:
        return False

    colchao([25,205,220],200,100)