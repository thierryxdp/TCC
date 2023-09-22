def soma_h(valor_h):
    H = 0
    for k in range(1,valor_h):
        H += (1/k)
    return round(H,2)