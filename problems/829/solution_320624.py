def soma_h(n):
    """função que retorna o valor da soma harmônica H com N termos
    int -> int"""
    H = 0
    for k in range(1,n+1):
        H += 1/k
    return H