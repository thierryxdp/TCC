def colchao(medidas, H, L):
    list.remove(medidas, max(medidas))
    if H >= L:
        if max(medidas) <= H and min(medidas) <= L:
            return true
        else:
            return false
    if L > H:
        if max(medidas) < L and min(medidas) < H:
            return true
        else:
            return false