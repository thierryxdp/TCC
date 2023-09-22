def bolos(A,B,C):
    """É necessário dividir a quantidade de ingrediantes que João tem a disposição
    com a quantidade necessária indicada pela receita para calcular a quantidade
    mínima de bolos que podem ser feitos com o que João possui."""
    return min(A//2,B//3,C//5)