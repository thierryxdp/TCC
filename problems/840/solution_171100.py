import math
def bolos(farinha, ovos, leite):
    """calcula o numero de bolos que joao conseguira fazer dado a quantidade de ingredientes que se tem disponiveis sendo a quantidade de farinha em xicaras e a de leite em colheres de sopa; int, int, int-> int"""
    xfarinha = (farinha//2)
    novos = (ovos//3)
    csleite = (leite//5)
    numbolos = math.floor(xfarinha, novos, csleite)
    return numbolos