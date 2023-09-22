bolos (a,b,c):
    """função que determina qual a quantidade máxima de bolobs que se pode fazer a partir dos ingredientes e do que se faz necessário na receita"""
    return min(math.floor(a/2,b/3,c/5))