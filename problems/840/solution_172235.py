def bolos( A, B, C):
    """caulcula a quantidade de bolos que pode ser feito com a quantidade de igredientes dadas"""
    
    quantidadeXicaras = A//2
    quantidadeOvos = B//3
    quantidadeColher = C//5
    
    return min(quantidadeXicaras, quantidadeOvos, quantidadeColher )