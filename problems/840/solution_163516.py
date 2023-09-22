def bolos(a,b,c):
    """Calcula a quantidade de bolos que João pode fazer com
       os ingredientes disponíveis, sendo estes (a),(b) e (c)"""
    return min(a//2,b//3,c//5)