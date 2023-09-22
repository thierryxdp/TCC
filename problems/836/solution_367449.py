def busca(setor, funcionarios):
    """Busca e retorna as informações de funcionários num dado setor.
    str, list -> list"""
    funcs_setor = []
    for i in range(len(funcionarios)):
        if str.upper(setor) == str.upper(funcionarios[i][2]):
            funcs_setor += [funcionarios[i][:2]+funcionarios[i][3]]
    return funcs_setor