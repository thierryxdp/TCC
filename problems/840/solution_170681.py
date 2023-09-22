def bolos(A,B,C):
    """ Função que recebe a quantidade de xícaras de farinha de trigo (A),
    	a quantidade de ovos (B) e a quantidade de colheres de sopa de leite (C)
    	calcula e retorna a quantidade máxima de bolos que podem ser feitos 
        em função da quantidade mínima de cada ingredientes."""
    return min(A//2,B//3,C//5)