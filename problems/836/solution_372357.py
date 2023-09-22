def busca(setor,m):
    """Retorna os dados dos funcionários do setor
    str,list-->list"""
    ret=[]
    for linha in m:
        for n in linha:
            if n==setor:
                list.append(ret,linha)
	for p in ret:
        list.remove(2,p)
    return ret