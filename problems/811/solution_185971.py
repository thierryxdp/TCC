def colchao(medidas, H, L):
    'retorna True em caso so colchão passar pela porta de False, caso contrário'
    if medidas[0] <= L and medidas[1] <= H:
        return True
    else:
        return False