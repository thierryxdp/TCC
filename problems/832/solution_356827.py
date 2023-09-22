def eh_quadrada(matriz):#Recebe uma matriz (Lista)
    num_linhas = len(matriz) 
    num_colunas = len(matriz[0])
    if num_colunas == num_linhas or matriz == [[]]:
        return True #Caso a quantidade de linhas e colunas da matriz forem iguais, a função retorna True
    return False #Caso a quantidade de linhas e colunas não forem iguais, a função retorna False