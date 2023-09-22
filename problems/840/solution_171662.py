def Bolos (A,B,C) :
    """ funcao que, dado as medidas de farinha de trigo (A),numeros de ovos (B) e numero de colheres de sopa de leite (C), retornara a quantidade maxima de bolo que joao consiguira fazer.
    int,int,int -> int """
    return min ((A//2),(B//3),(C//5))