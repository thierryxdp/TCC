def busca(setor_busca, M):
    '''Função que dado um setor e uma matriz, retorna os dados dos funcionários
    que trabalham naquele setor
    str, list -> list'''
    dados = []
    for nome, registro, setor in M:
        if setor == setor_busca:
             dados.append([nome, registro, fone])
    return dados