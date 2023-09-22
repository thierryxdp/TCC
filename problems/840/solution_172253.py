def bolos( a, b, c):
    """caulcula a quantidade de bolos que pode ser feito com a quantidade de igredientes dadas"""
    
    qtd_farinha = a//2
    qtd_ovo = b//3
    qtd_leite = c//5
    
    return min(qtd_farinha , qtd_ovo , qtd_leite )