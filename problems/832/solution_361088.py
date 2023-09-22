def eh_quadrada(m):
    """ funcao que recebe uma matriz "m" de entrada, e retorna um valor
    booleano "True" caso ela seja quadrada ou "False" caso não seja """
    """ list -> bool"""
    for linha in range(0,len(m)):
        for coluna in range(0,len(m[linha])):
            if len(m)==len(m[linha]) and len(m[coluna]):
                return True
            else:
                return False
    return True
#casos de teste:
"""eh_quadrada([[0,1],[0,2]])
>>> True
   eh_quadrada([[0,1,2],[1,1,1],[2,3,4]])
>>> True
   eh_quadrada([])
>>> True
   eh_quadrada([[1,1,1]])
>>> False