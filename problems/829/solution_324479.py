def soma_h(valor_h):
    if valor_h == 0:
        return 1
    H = 0
    for k in range(1,valor_h+1):
        H += (1/k)
    return round(H,2)