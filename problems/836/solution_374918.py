def busca(empresa_sector,dados_matriz):
    '''
    funcao que retorna as informacoes de todas as pessoas de um mesmo setor da empresa ao inserir uma matriz
    com os dados de todos os setores da empresa, no formato de lista
    str,list->list
    '''
    pessoas_sector=[]
    for x in range(len(dados_matriz)):
        if empresa_sector in dados_matriz[x]:
            pessoas_sector=pessoas_sector+[dados_matriz[x]]
          
    for y in range(len(pessoas_sector)):
    	if empresa_sector in pessoas_sector[y]:
            list.remove(pessoas_sector[y],empresa_sector) 
            
    return pessoas_sector