def busca(setor_buscado, matriz):
    func_setor = []
    for funcionario in matriz:
        setor_atual = funcionario[2]
        if setor_atual == setor_buscado:
            func_setor.append(funcionario)
    return func_setor