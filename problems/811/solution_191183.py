def questãoimpossivel(dimensões:list,H,L):
    if dimensões[0]<=L and dimensões[2]<=H:
        return True
    if dimensões[0]<=H and dimensões[2]<=L:
        return True
    if dimensões[0]<=L and dimensões[1]<=H:
        return True
    if dimensões[0]<=H and dimensões[1]<=L:
        return True
    if dimensões[1]<=L and dimensões[2]<=H:
        return True
    if dimensões[1]<=H and dimensões[2]<=L:
        return True
    else:
        return False