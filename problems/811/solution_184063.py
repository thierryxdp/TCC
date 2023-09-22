def colchao(lista,H,L):
    if (lista[0] < H and lista[1] < L) or (lista[1] < H and lista[0] < L):
        return True
    else:
        return False