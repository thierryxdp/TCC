def busca(matriz,setor):
    '''busca funcionários por setor, retornando todos os 
    dados dos funcionários daquele setor; list -> list'''
    ListaFinal = []
    linhas = len(matriz)
    colunas = len(matriz[0])
    for i in linhas:
        for j in colunas:
            if matriz[i][2] == setor:
                ListaFinal.append(matriz[i])
            else:
                ListaFinal
        return ListaFinal