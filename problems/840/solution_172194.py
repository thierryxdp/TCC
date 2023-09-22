def bolos(a,b,c):
    """Função que recebe como parâmetros o número de xícaras
    de farinha de trigo, o número de ovos e o número de 
    colheres de sopa de leite, respectivamente, e retorna o 
    número máximo de bolos que podem ser feitos."""
    a = a//2
    b = b//3
    c = c//5
    
    if (a < b and a < c):
        return a
    elif (b < a and b < c):
        return b
    elif (c < a and c < b):
        return c