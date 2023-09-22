def busca(setor,matriz):
    '''Esta função tem como entrada uma lista com dados de funcionários
    (matriz) e o setor que se deja buscar nessa lista.
    É retornado os dados de todos os funcionários do setor buscado.
    list, str -> list'''
    
    linhas= len(matriz)
    resultado= []
        
    for i in range(linhas):
        setor_funcionario=matriz[i][2]
        if setor in setor_funcionario:
            del matriz[i][2]
            list.append(resultado, matriz[i])
               
    return resultado