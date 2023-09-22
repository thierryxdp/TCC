def busca(setor,matriz):
    '''faz uma busca por setor dado seu nome, retornando os dados dos funcionarios do que nele trabalham;
    matriz->lista'''
    lista=[]
    for i in range(len(matriz)):
        if matriz[i][2]==setor:
            list.append(lista,matriz[i])
            if len(lista)<i:
                del lista[i][2]
    return lista