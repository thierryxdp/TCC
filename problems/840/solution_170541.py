def bolos(a,b,c):
    """retorna a quantidade de bolos que podem ser feitos dados a quantidade de farinha a, ovos b e colheres de leite c """
    return min(round(a/2) , round(b/3) , round(c/5))