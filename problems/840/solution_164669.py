def bolos(a,b,c):
    """Calcula e retorna a quantidade máxima de bolos que podem ser feito.
    Dado a quantidade de xícaras de farinha de trigo, número de ovos e numero de colheres de sopa. int/float,int/float,int/float->int/float"""
    return min(a//2,b//3,c//5)