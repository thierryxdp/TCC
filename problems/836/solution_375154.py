def busca(setor,matriz):
    '''função que dada uma matriz, procura por setor os dados
    de cada funcionario;
    matriz-> lista'''
    dados=[]
    for i in matriz:
        if i[2]==setor:
            dados.append(i[0:2]+i[3:])
    return dados