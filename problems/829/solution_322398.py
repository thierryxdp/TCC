def soma_h(N):
    """retorna o valor de H em:
       H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N"""
    """int -> int"""
    
    i = 1
    H = 0
    while i <= N:
        H += 1/i
        i += 1
    return round(H,2)