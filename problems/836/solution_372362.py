def busca(setor,m):
    """Retorna os dados dos funcionários do setor
    str,list-->list"""
    ret=[]
    for linha in m:
        for n in linha:
            if n==setor:
                list.remove(linha,setor)
                list.append(ret,linha)
    return ret