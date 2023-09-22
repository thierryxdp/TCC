def bolos (A,B,C):
    """ Calcula o número máximo de bolos que podem ser feitos (: int) com os números de entrada A
(xícaras de farinha), B(ovos) e C(colher de sopa de leite):floats. Retorna a divisão de A por 2, B
por 3 e C por 5, que são as medidas mínimas para realizar um bolo."""
    return min(A//2,B//3,C//5)