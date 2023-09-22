def busca(setor,matriz):
    """Recebe uma matriz e um setor e faz uma busca no setor, retornando 
    os dados de todos os funcionários do local determinado"""
    funcionarios = []
    for funcionario in matriz:
        if funcionario[2] == setor:
            pessoa = [funcionario[0],funcionario[1],funcionario[3]]
            list.append(funcionarios,pessoa)
    return funcionarios