def busca(setor,matriz):
    """Retorna os dados de todos os funcinários do setor
    desejados;
    str, list-> list"""
    n_linhas = len(matriz)
    funcionarios=[]
    
    for i in range(n_linhas):
        if setor in matriz[i]:
            list.append(funcionarios, list.remove(matriz[i],setor))
       
    return funcionarios