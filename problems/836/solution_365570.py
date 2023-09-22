def busca(setor, matriz):
    """Dada uma database de empresa no formato
    [Nome, registro, setor, telefone], pede o setor
    e a lista de funcionários e retorna todos os funcionários
    daquele setor.
    str, list->list"""
    resultado_busca = []
    for funcionarios in matriz:
        if setor in funcionarios[2]:
            resultado_busca.append([funcionarios[0],funcionarios[1],funcionarios[3]])
    return resultado_busca