def busca(setor, m):
    '''
    	Função que recebe uma matriz como a do exemplo e faça uma busca
        por setor, ou seja, dado um nome de um setor da empresa,
        a função retorna os dados de todos os funcionários daquele setor.
        OBS:Se nenhum registro for encontrado, a função deverá retornar uma lista vazia.
        i:int
        res:list
        return:list 
    '''
    i = 0
    res = []
    while i < len(m):
        if m[i][2] == setor:
            res.append([m[i][0], m[i][1], m[i][3]])
        i += 1
    return res