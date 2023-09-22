def receita_de_bolo (A,B,C):
    """calcula o numero maximo de bolos possiveis de serem feitos com os ingredientes especificos A,B,C
    entrada:
    A,B,C: int
    A=farinha
    B= ovos
    C= colheres de leite
    saida
    int
    quantidade maxima de bolos possiveis 
    """
    return min (A//2,B//3,C//5)