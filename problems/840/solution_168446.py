def bolos (A,B,C):
    '''Calcula a quantidade maxima de bolos que Joao consegue fazer, 
    dadas as variaveis (A,B e C) para xicaras de farinha de trigo, ovos
    e colheres de sopa de leite, respectivamente
    int, int, int -> int '''
    if A//2 >= 1:
        if B//3 >= 1:
            if C//5 >= 1:
                return min((A//2), (B//3) , (C//5))
    if A//2 <= 0:
        return (0)
    if B//3 <= 0:
        return (0)
    if C//5 <= 0:
        return (0)