def busca(setor,matriz):
    '''Funcao que retorna uma lista que contem
    os dados dos funcionarios que pertencem ao 
    setor indicado.
    '''
    lista_dados = []
    for i in range(len(matriz)):
        if setor == matriz[i][2]:
            lista_dados.append([matriz[i][0],matriz[i][1],matriz[i][3]])
    return lista_dados