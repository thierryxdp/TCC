def busca(setor, matriz):
    '''Retorna os dados de todos os funcionários de determinado setor
    	str, list(list) -> list(list)'''
    dados = []
    for linha in matriz:
        if linha[2] == setor:
            del linha[2]
            dados.append(linha)
    return dados