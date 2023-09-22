def colchao(medidas, H, L):
    """Fun ̧c~ao define se colch~ao passa pela porta
    de acordo com as medidas do colch~ao.
    list, float, float--> bool"""
    if medidas[1] <= H:
        return True
    if medidas[1] <= L:
        return True
    if medidas[2] <= H:
        return True
    if medidas[2] <= L:
        return True
    else:
        return False