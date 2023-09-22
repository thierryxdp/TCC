def qtd_bolos (A, B, C):
    """
    Descrição: Recebe as quantidades de farinha de trigo, ovos e leite. Em
    seguida, calcula e retorna quantos bolos é possível fazer com as quantidades
    de ingredientes informadas

    Parâmetros:
        A, B, C -> int
        Número de xícaras de farinha, ovos e colheres de sopa de leite,
        respectivamente.

    Retorno:
        Número de bolos -> int 
    """
    return int(min(A/2, B/3, C/5))