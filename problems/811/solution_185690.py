def colchao(medidas,H,L):
    """função que retorna a possibilidade de um colchão de dimensões AxBxC
    passar por uma porta de altura H e largura L;
    Entrada: lista, int, int
    Saída: bool"""
    x=medidas
    if x[1]<=H or x[1]<=L:
        return True
    if x[2]<=H or x[2]<=L:
        return True
    else:
        return False