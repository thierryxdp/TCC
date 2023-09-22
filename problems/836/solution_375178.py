def busca(setorbusca,matriz):
    '''Essa função dada uma matriz, procura um setor 
    nela e retorna informações referente a esse setor, 
    list->list'''
    dados = []
    for nome, registro, setor, telefone in matriz:
        if setor == setorbusca:
             dados.append([nome, registro, telefone])
    return dados