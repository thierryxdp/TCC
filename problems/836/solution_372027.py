def busca (area, matriz):
    '''dado um nome de um setor da empresa, a funcao retorna os dados de todos os funcionarios daquele setor'''
    resultado = []
    for lin in range(0, len(matriz)):
        for col in range(0, len(matriz[lin])):
            if area.lower() == matriz[lin][col].lower():
                dados = matriz[lin].copy()
                dados.pop(dados.index(dados[col]))
                resultado.append(dados)
    return resultado