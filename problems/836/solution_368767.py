def busca(setor,matriz):
    '''Função que dado um setor e uma matriz de funcionarios
    retorna as informações dos funcionários pertencentes à aquele
    setor. list,str -> list'''
    Lista = []
    for i in matriz:
        if setor in i:
                Lista = Lista + [i[0]+i[1]+i[3]]
    return Lista