def colchao(Dimensoes,H,L):
    if Dimensoes [0] <= H and Dimensoes [1] <= L or Dimensoes [0] <= H and Dimensoes [2] <= L or Dimensoes [1] <= H and Dimensoes [2] <= L or Dimensoes [2] <= H and Dimensoes [1] <= L or Dimensoes [0] <= L and Dimensoes [1] <= H or Dimensoes [0] <= L and Dimensoes [2] <= H:
        return True
    else:
        return False