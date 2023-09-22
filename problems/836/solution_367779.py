def busca(setor,matriz):
    """..."""
    
    lista_retorno = []
    
    for i in range(len(matriz)):
        dados_funcionario = []
        for j in range(len(matriz[0])):
            if matriz[i][j] == setor:
                list.append(dados_funcionario,matriz[i][0])
                list.append(dados_funcionario,matriz[i][1])
                list.append(dados_funcionario,matriz[i][3])
        list.append(lista_retorno,dados_funcionario)
    return lista_retorno