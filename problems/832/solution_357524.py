def eh_quadrada (matriz):
    """funçao que recebe uma matriz e retorna true se o numero de colunas for igual ao numero de linha e false se nao;
    entrada: list;
    saida: bool."""
    L= len(matriz)
    C =len(matriz[])
    if matriz == []:
        return True
    if L == C:
        return True
    else:
        return False