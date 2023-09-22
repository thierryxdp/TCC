def eh_quadrada(matriz):#Recebe uma matriz (Lista)
    for linha in matriz:
        linha.append(1)

    if matriz == [[1]]:
        return True
    
    for linha in matriz:
        linha.remove(1)

    num_linhas = len(matriz) 
    num_colunas = len(matriz[0])
    if num_colunas == num_linhas:
        return True #Caso a quantidade de linhas e colunas da matriz forem iguais, a função retorna True
    return False #Caso a quantidade de linhas e colunas não forem iguais, a função retorna False