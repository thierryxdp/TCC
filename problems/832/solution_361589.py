def eh_quadrada(m):
    """A função retorna se a matriz dada como parâmetro é quadrada (quando o 
       número de linhas é igual ao número de colunas) ou não.
       list -> bool"""
    if len(m) == 0:
        return True
    elif len(m) != 0:
        if len(m) == len(m[0]):
            return True
        else:
            return False
#Testes:
#m = []
#eh_quadrada(m)--> True

#m = [[1, 2, 3], [2, 3, 4]]
#eh_quadrada(m)--> False

#m = [[1, 2], [3, 4]]
#eh_quadrada(m)--> True