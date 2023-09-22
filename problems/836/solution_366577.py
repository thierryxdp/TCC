def busca(setor, matriz):
    """Função que faz uma busca por setor e retorna os dados de todos os 
    funcionários daquele setor. list, str -> list"""
    retorno = []
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            a = matriz[i][:2] + matriz[i][3:]
            retorno = retorno + list(a)
    return retorno