def busca(string, m):
    '''Funcao recebe uma string e umamatriz contendo uma lista de contatos de diversos setores de uma empresa e retorna uma lista contendo todos os funcionarios daquele setor representado pela string
string, list -> list'''
    funcionarios = []
    for i in m:
        if (string == i[2]):
            novalista = [i[:2] + i[3:]]
            list.append(funcionarios, novalista)
    return funcionarios