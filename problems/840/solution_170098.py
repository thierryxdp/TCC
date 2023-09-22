def bolos(a=2,b=3,c=5):
    """funcao que retorna o numero maximo de bolos possiveis,sendo a(xicaras de farinha de trido),b(ovos),c(colheres de sopa de leite)"""
    import math
    return math.floor ((a//2)+(b//3)+(c//5))//5