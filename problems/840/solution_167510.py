def bolos(A,B,C):
    """Retorna a quantidade máxima de bolos possíveis a serem
    feitos dadas as entradas A (xícaras de farinha), B (ovos)
    e C (colheres de leite) como ingredientes
    int, int, int - > int"""
    return (A//2 + B//3 + C//5)//3