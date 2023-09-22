def busca(setor, matriz):
    '''Dada uma matriz com os dados dos funcionários de
    uma empresa e o nome de um setor, retorna os dados
    dos funcionários daquele setor
    str, list -> list'''
    funcionarios = []
    for i in range(len(matriz)):
        if setor == matriz[i][2]:
            funcionarios.append([matriz[i][0], matriz[i][3]])
    return funcionarios