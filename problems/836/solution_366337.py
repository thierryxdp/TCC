def busca(setor, matriz):
    '''
    Busca os dados de todos os funcionários de certo setor de uma empresa .
    str, list -> list

    Parameters:
    setor: Parâmetro textual do tipo string (str);
    matriz: Parametro do tipo lista (list).

    Returns:
    A lista com as informações de todos os funcionários de determinado setor da empresa. 
    '''

    linhas = len(matriz)
    colunas = len(matriz[0])
    
    for i in range(linhas):
        for j in range(colunas):
            if type(matriz[i][j]) != str:
                return ("Utilize somente valores textuais para os elementos da matriz. Tente novamente!")
            
    setor = str.lower(setor)
    matriz_buscada = []


    for i in range(linhas):
        matriz[i][2] = str.lower(matriz[i][2])
        if matriz[i][2] == setor:
            del matriz[i][2]
            list.append(matriz_buscada, matriz[i])

    return matriz_buscada