def busca(setor, matriz):
    """Dados por entrada o setor de interesse e a matriz
    respectivamente, a função retornará uma matriz com os dados de
    todos os funcionários daquele setor.
    str, matriz -> matriz"""
    
    linhas = len(matriz)
    colunas = len(matriz[0])
    nova_matriz = []
    
    for i in range(linhas):
        if matriz[i][2] == setor:
            dados = matriz[i][0:2]+matriz[i][3:]
            nova_matriz = nova_matriz + [dados]
    
    return nova_matriz