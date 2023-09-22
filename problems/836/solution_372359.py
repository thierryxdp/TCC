def busca(setor,m):
    """Retorna os dados dos funcionários do setor
    str,list-->list"""
    ret=[]
    for linha in m:
        for n in linha:
            if n==setor:
                list.remove(2,linha)
                list.append(linha,ret)
    return ret