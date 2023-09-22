# Dada matriz com dados dos funcionários e o nome
# de um setor, queremos as informações dos funcionários
# desse setor.
# Resolução:
# 1. Para cada funcionário, verifica o setor;
# 2. Se o setor for o solicitado, adiciona seus dados
#    à lista com os funcionários do setor;
# 3. Devolve a lista

def busca(setor: str, matriz: list) -> list:
    '''Dada matriz com dados dos funcionários e o nome
    de um setor, retorna as informações dos funcionários
    desse setor'''
    funcionarios = []
    for funcionario in matriz:
        if (funcionario[2] == setor):
            func_setor = funcionario[:2] + funcionario[3]
            list.append(funcionarios, func_setor)
    return funcionarios