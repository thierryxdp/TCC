def busca(dados,setor):
    '''Função que, dado o setor de uma empresa e a relação dos dados dos funcionários, retorna os dados dos funcionários daquele setor.
    list, str --> list'''
    dados_pessoais = []
    resultado = []
    for x in dados:
        if x[2] == setor:
            dados_pessoais = [[x[0]] +[x[1]] + [x[3]]]
            resultado = resultado + dados_pessoais
    return resultado