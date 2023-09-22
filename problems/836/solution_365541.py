def busca(setor, matriz):
    ''' dada a matriz de 4 colunas com as informacoes dos funcionarios de uma empresa na ordem: nome, registro, setor e telefone e o setor desejado, retorna as os dados dos funcionarios daquele setor
    matriz, str -> matriz'''
    resultbusca = []
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            resultbusca = resultbusca + matriz[i][0:2]+[matriz[i][3]]
    return [resultbusca]