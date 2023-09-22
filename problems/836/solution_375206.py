def busca(setor,dados):
    """doc"""
    funcionarios = []
    for funcionario in dados:
        if setor == funcionario[2]:
            funcionarios.append([funcionario[0],funcionario[1], funcionario[3]])
    return funcionarios