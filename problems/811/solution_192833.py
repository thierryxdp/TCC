def colchao(medidas, H, L):
    ''''''
    a, b, c = medidas
    a = [0]
    b = [1]
    c = [2]
    if a <= H and b <= L:
        True
    elif a <= H and c <= L:
        True
    elif b <= H and a <= L:
        True
    elif b <= H and c <= L:
        True
    elif c <= H and a <= L:
        True
    elif c <= H and b <= L:
        True
    else:
        False