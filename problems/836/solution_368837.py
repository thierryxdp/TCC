def busca(setor,matriz):
    '''Esta função tem como entrada uma lista com dados de funcionários
    (matriz) e o setor que se deja buscar nessa lista.
    É retornado os dados de todos os funcionários do setor buscado.
    list, str -> list'''
    
    linhas= len(matriz)
    colunas= len(matriz[0])
    resultado= []
        
    for i in range(linhas+1):
        setor_funcionario=matriz[i][2]
        if setor in setor_funcionario:
            list.append(resultado, matriz[i])
            del resultado[i][2]   
    return resultado