def busca(setor,m):
    """Retorna os dados dos funcionários do setor
    str,list-->list"""
    ret=[]
    for linha in m:
        for n in linha:
            if n==setor:
                list.append(ret,linha[0])
                list.append(ret,linha[1])
                list.append(ret,linha[3])
    return ret