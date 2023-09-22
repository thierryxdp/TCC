def bolos(A, B, C):
    """Função que calcula quantos bolos João consiguirá fazer, dadas as quantidades de xícaras de farinha (A), de ovos (B), em número inteiro, e de colheres de sopa de leite (C), em número inteiro
    Valores de entrada: int, int, int
    Valor de saida: int"""
    return min(A//2, B//3, C//5)