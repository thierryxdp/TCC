def busca(nome_setor,matriz):
    '''funcao que recebe uma matriz representando as informacoes de um funcionario e um nome de um setor da empresa como entrada e retorna os dados de todos os funcionarios daquele setor
str, list(list) -> list'''
    informacoes=[]
    for linha in range(len(matriz)):
        setor=matriz[linha][2]
        if setor==nome_setor:
            informacoes+=matriz[linha]
    return informacoes