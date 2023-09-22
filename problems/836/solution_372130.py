def busca(setor,matriz):
    '''
       funcao que recebe um setor da empresa e uma matriz e
       retorna os dados de todos os funcionarios daquele 
       setor contidos na matriz
       str, list -> list
    '''
    nlinhas = len(matriz)
    ncolunas = len(matriz[0])
    linha = []
    for i in range(nlinhas):
        for j in range(ncolunas):
            if setor == matriz[i][j]:
                
                linha.append([matriz[i][0],matriz[i][1],matriz[i][3]])
    return linha