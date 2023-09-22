def colchao(medidas,H,L):

  if medidas[0] <= H or medidas[0] <= L:

    if medidas[1] <= L or medidas[2] <= L:

      return True

    elif medidas[1] <= H or medidas[2] <= H:

      return True

    else:

      return False 

  else:

    if medidas[1] <= H and medidas[2] <= L:

      return True

    elif medidas[1] <= L and medidas[2] <= H:

      return True

    else:

      return False