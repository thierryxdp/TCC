def bolos(A: int, B: int, C: int) -> int:
    '''
    Retorna quantidade máxima de bolos possíveis de serem feitas por João, dado a quantidade de
    ingredientes [A (xícaras de farinha de trigo), B (ovos) e C (colheres de sopa de leite)]
    '''
    farinha = A // 2
    ovos = B // 3
    leite = C // 5
    return min(farinha, ovos, leite)