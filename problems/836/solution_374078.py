def busca(setor,matriz):
    '''Funcao retorna os dados de todos os funcionarios
    que trabalham em um mesmo setor;str,list->list'''
    dados=[]
    for i in range(len(matriz)):
        if setor in matriz[i]:
            nome=matriz[i][0]
            registro=matriz[i][1]
            telefone=matriz[i][3]
            resultado=[nome,registro,telefone]
            dados.append(resultado)
    return dados