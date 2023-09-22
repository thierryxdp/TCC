def busca(setor,mat):
    '''Recebe uma matriz contendo os dados dos funcionários
    e o setor desejado. Retorna uma lista com os dados de 
    todos os que trabalham no setor.
    list, str -> list'''
    i = 0
    lista_setor = []
    while i < len(mat):
        if setor in mat[i]:
            list.append(lista_setor,mat[i])
    	i += 1
    return lista_setor