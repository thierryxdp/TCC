def colchao(medidas,H,L):
    """
    Função que recebe as medidas de um colchão e as medidas de uma porta
    e retorna um valor booleano: True se o colchão conseguir passar pela porta e False
    caso contrário.
    list, int, int -- bool
    """
    a,b,c=medidas
    return min(b,c)<=max(H,L)