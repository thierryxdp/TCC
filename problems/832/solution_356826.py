def eh_quadrada(matriz):#Recebe uma matriz (Lista)
    if matriz == [[]]:
        return True #Caso em que será apresentado Index out of range na linha 5, como a questão mesma disse, esse caso específico é True
    num_linhas = len(matriz) 
    num_colunas = len(matriz[0])
    if num_colunas == num_linhas:
        return True #Caso a quantidade de linhas e colunas da matriz forem iguais, a função retorna True
    return False #Caso a quantidade de linhas e colunas não forem iguais, a função retorna False