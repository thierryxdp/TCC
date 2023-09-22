def busca(a,m):
    """funcao que retorna os dados dos funcionarios de
    um setor, dado o setor. str,list->list"""
    x=[]
    for p in m:
        for q in p:
            if q==a:
                list.remove(p,q)
                list.append(x,p)
    return x