def busca(setor, matriz):
    """Dada uma database de empresa no formato
    [Nome, registro, setor, telefone], pede o setor
    e a lista de funcionários e retorna todos os funcionários
    daquele setor.
    str, list->list"""
    resultado_busca = []
    for funcionarios in matriz:
        linha = []
        if setor in funcionarios[2]:
            linha.append([funcionarios[0],funcionarios[1],funcionarios[3]])
            resultado_busca.append(linha)
    return resultado_busca