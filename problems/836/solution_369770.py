def busca(matriz,setor):
    '''busca funcionários por setor, retornando todos os 
    dados dos funcionários daquele setor; list -> list'''
    ListaFinal = []
    linhas = len(matriz)
    for i in range(linhas):
        colunas = len(matriz[i])
        for j in range(colunas):
            if matriz[i][2] == setor:
                ListaFinal.append(matriz[i])
            else:
                ListaFinal 
        return ListaFinal