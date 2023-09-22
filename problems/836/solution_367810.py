def busca(setor, registro):
    '''Retorna todos os funcionários do setor escolhido
str, list -> list'''
    saida = []
    for funcionario in registro:
        if funcionario[2] == setor:
            saida.append( funcionario[0:2] + [funcionario[3]] )
    return saida