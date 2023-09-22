def busca(matriz, setor):
    """Funcao que dado um nome de um setor da empresa, retorna os dados de 
       todos os funcionarios daquele setor, se nenhum registro for encontrado,
       a funçao deve retornar uma lista vazia."""
    funcionario = []
    for funcao in matriz:
        if funcao[2] == setor:
            list.append(funcionario, funcao[:2] + funcao[3:])
    if funcionario != []:
        return funcionario
    return []