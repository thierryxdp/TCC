def colchao(medidas, H, L):
    """Função que determina se é possível ou não passar um colchão por uma porta;
    list, int, int -> bool"""
    if medidas[1] < H:
            return True
    else:
        if medidas[1] < L:
            return True
        else:
            return False