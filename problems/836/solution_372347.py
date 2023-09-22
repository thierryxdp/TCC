def busca(setor,m):
    """Retorna os dados dos funcionários do setor
    str,list-->list"""
    ret=[]
    for linha in m:
        if setor in linha:
            list.append (linha,ret)
    return ret