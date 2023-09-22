def bolos(A,B,C):
    """Calcula e retorna a quantidade máxima de bolos que podem
    ser feitos a partir de uma receita dada e tendo como entrada
    os valores disponíveis de A xícares de farinha de trigo, B 
    e C colheres de sopa de leite
    int ou float, int ou float, int ou float -> int"""
    return min(A//2,B//3,C//5)