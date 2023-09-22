def busca(setor, matriz):
    '''função que retorna funcionários com informações na matriz que estão no setor recebido na entrada.
    string, list -> list'''
    
    buscados = []
    
    for i in range(len(matriz)):
        if setor in matriz[i]:
            list.append(buscados, matriz[i])
    return buscados