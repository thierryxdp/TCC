def busca(setor,matriz):
    """funcao que dado o nome do setor retorne as informacoes dos funcionarios correspondente.
    str,list(list)->list(list)."""
    lista=[]
    for i in matriz:
        if setor in i:
            lista=lista+[i[0],i[1],i[3]]
    return lista