def busca(s,m):
    '''Dado uma string contendo o setor e uma matriz com
    todas as informações de todos os funcionários, retorna 
    os dados de todos os funcionários daquele setor.
    list -- list'''
    dados = []
    
    for fun in m:
        if fun[2] == setor:
            list.append(dados,fun[:2]+fun[3:])
    if dados != []:
        return dados
    return []