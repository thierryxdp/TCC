def busca (setor, matriz):
    """Função que recebe uma matriz em que cada linha representa um funcionário, tendo 4 colunas
    para as seguintes informações respetivamete: nome, registro, setor e telefone. Além disso, a 
    função também recebe o nome do setor que se deseja buscar. A função retorna os dados de todos
    os funcionários que trabalham naquele setor.
    str, matriz -> list"""
    resultado = []
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            matriznova = [[matriz[i][0],matriz[i][1],matriz[i][3]]]
            resultado = resultado + matriznova
    return resultado