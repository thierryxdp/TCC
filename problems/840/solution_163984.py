def bolos(A,B,C):
    """Esta é a função que dadas as quantidades dos ingredientes disponíveis, retorna quantos bolos serão possíveis fazer"""
    return min(A/2,B/3,C/5)