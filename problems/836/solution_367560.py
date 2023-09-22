def busca(setor,matriz):
    '''Funcao que retorna uma lista que contem
    os dados dos funcionarios que pertencem ao 
    setor indicado.
    '''
    lista_dados = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if setor == matriz[i][j]:
                lista_dados.append(matriz[i])
                lista_dados.del(lista_dados[2])
    return lista_dados