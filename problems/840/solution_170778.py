import math
def bolos(a,b,c):
    """função que dados a quatidade "a" de xic. de farinha, "b" de ovos e "c" de colheres de sopa de leite, calcula e retorna a quantidade exata de bolos que se pode fazer"""
    if ((a>=2)and(b>=3)and(c>=5)):
        return min(math.floor((a/2),(b/3),(c/5)))
    else:
        return (0)