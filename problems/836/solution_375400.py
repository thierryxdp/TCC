def busca(setor,matriz):
    '''dada uma matriz com nome,registro,setor e 
    telefone por linha e um setor que queremos encontrar
    a funcao retorna os dados de todos os funcionarios
    daquele setor
    matriz -->list'''
    juncao = []
    for i in matriz:
        for k in i:
            if k == setor:
                juncao += matriz[i]
    return juncao