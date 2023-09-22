def busca(setor,M):
    '''dada uma matriz e um determinado setor de uma empresa,
    retorna os dados dos funcionarios daquele setor;
    list->list'''
    linha=0
    dados=[]
    for i in M:
        if setor in M[linha]:
            dados_f=[M[linha][0],M[linha][1],M[linha][3]]
            list.append(dados,dados_f)
        linha+=1
    return dados