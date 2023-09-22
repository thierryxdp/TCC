def bolos(A, B, C):
    # Função que pega o número de ingredientes que o usuário tem e retorna o número de bolos que ele consegue fazer
    # int, int, int -> int
    return min(A // 2, B // 3, C // 5)