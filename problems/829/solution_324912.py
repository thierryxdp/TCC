def soma_h(N):
    """int -> float"""
    """retorna a soma dos n termos da sequencia 1/n"""
    
    H = 0
    
    for n in range(1,N+1):
        H += 1/n
        pass
    return H