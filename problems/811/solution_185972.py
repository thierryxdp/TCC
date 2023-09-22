def colchao(medidas, H, L):
    'retorna True em caso so colchão passar pela porta de False, caso contrário'
    if H >= L:
        if medidas[0] <= L and medidas[1] <= H:
            return True
        else:
            return False
    else:
        if medidas[0] <= H and medidas[1] <= L:
            return True
        else:
            return False