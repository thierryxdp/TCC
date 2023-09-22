def busca(setor,matriz):
    """Dados o setor e a matriz que guarda os dados dos funcionários de uma empresa, respectivamente, a função nos retorna os dados de todos os funcionários que trabalham neste setor; string, list -> list"""
    
    lista_retorno = []
    
    for i in range(len(matriz)):
        dados_funcionario = []
        for j in range(len(matriz[0])):
            if matriz[i][j] == setor:
                list.append(dados_funcionario,matriz[i][0])
                list.append(dados_funcionario,matriz[i][1])
                list.append(dados_funcionario,matriz[i][3])
                
        if dados_funcionario != []:
                list.append(lista_retorno,dados_funcionario)
                
    return lista_retorno