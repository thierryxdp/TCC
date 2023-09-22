def busca(nome_setor, matriz):
    retorno = []
    for funcionario in matriz: # [nome, registro, setor, telefone]
        if funcionario[2] == nome_setor:
            retorno.append(funcionario.remove(nome_setor))
    return retorno