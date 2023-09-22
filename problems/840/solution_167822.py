def quantidade_bolos(A, B, C):
    """ retorna a quantidade de bolos que se pode fazer com a qauntidade A de xicras de farinha, B de ovos e C de colheres de sopa de leite, levando em conta as medidas da receita:
    int, int,int-> int """
    if (A//2) and (B//3) and (C//5)>=1:
        return min((A//2), (B//3), (C//5))
    else:
        return 0