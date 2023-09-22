def bolos(f,o,s):
    """essa função calcula a quantidade de bolos que joão pode fazer com os ingredientes que tem em casa;
    int,int,int--->int"""
    return min(f//2,o//3,s//5)