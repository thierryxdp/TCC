def bolos_pingredientes(A,B,C)
    """funcao que dada a quantidade disponivel dos ingredientes A,B e C retorna
    quantos bolos é possível fazer (contando os ingredientes separadamente)"""
    return ((A//2),(B//3),(C//5))
def bolos(A,B,C):
    """funcao que dada a quantidade disponivel dos ingredientes A,B e C retorna
    quantos bolos é possível fazer"""
    return min(bolos_pingredientes(A,B,C))