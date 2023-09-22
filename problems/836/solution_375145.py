def busca(setor, matriz):
    funcionarios = []
    for funcionario in matriz:
        if funcionario[2] == 'setor':
            funcionarios.append( [funcionario[0], funcionario[1], funcionario[3]] )
    return funcionarios