def busca(nome_setor,matriz):
    '''funcao que recebe uma matriz representando as informacoes de um funcionario e um nome de um setor da empresa como entrada e retorna os dados de todos os funcionarios daquele setor
str, list(list) -> list'''
    informacoes=[]
    for linha in matriz:
        nome=matriz[linha][0]
        registro=matriz[linha][1]
        setor=matriz[linha][2]
        telefone=matriz[linha][3]
        if setor==nome_setor:
            informacoes+=[nome,registro,telefone]
    return informacoes