def busca(setor,matriz):
    '''Função que recebe uma string com o setor e uma matriz com
    informaçẽs de todos os funcionarios da empresa, e retorna os
    dados de todos os funcioanrios daquele setor.
    list -> list'''
    
    dados = []
    
    for funca in matriz:
        if funca[2] == setor:
            list.append(dados, funca[:2] + funca[3:])
    
    if dados != []:
        return dados
    
    return []