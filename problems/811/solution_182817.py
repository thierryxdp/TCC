def colchao(medidas,H,L):
    """Retorna se o colchão passará ou não com base nas medidas dadas; lista, int, int-> bool."""
    if int(medidas[:1:])<=H and int(medidas[1:2:])<=L:
        return True
    elif int(medidas[:1:])<=H and int(medidas[2::])<=L:
        return True
    elif int(medidas[1:2:])<=H and int(medidas[2::])<=L:
        return True
    elif int(medidas[:1:])<=H and int(medidas[2::])<=L:
        return True
    elif int(medidas[1:2:])<=H and int(medidas[:1:])<=L:
        return True
    elif int(medidas[2::])<=H and int(medidas[:1:])<=L:
        return True
    elif int(medidas[2::])<=H and int(medidas[1:2:])<=L:
        return True
    else:
        return False