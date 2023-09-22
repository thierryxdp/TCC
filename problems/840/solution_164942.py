import builtins

def bolos(A,B,C):
    ''' Função que retorna a quantidade máxima de bolos que podem
    ser feitos dados a quantidade de xícaras de farinha (A), ovos
    (B) e colheres de sopa de leite (C)
    int, int, int -> int '''
    return builtins.min(A//2,B//3,C//5)