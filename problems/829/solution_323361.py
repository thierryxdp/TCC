def soma_h(N):
    """Retorna a soma de H, de N termos. (int->float)"""
    H=0
    for i in range(N):
        H=H+((i+1)**(-1))
    return round(H,2)