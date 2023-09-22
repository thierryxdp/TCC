def colchao(medidas,H,L):

    if medidas[0] < H:

        if medidas[1] < L:

            return True
        elif medidas[2] < L:

            return True
    elif medidas[1] < H:

        if medidas[0] < L:

            return True
        
        elif medidas[2] < L:

            return True
    
    elif medidas[2] < H:

        if medidas[0] < L:

            return True
        
        elif medidas[1] < L:

            return True
    else:

        return False