def total(lis, dic):
    """Função que recebe uma lista e um dicionário e
retorna a soma das chaves da lista que estão no dicio.
"""
    ndi = {}
    for x in range (0, len(lis), 1):
    	if lis[x] in dic:
        	ndi[lis[x]] = dict.get(dic, lis[x])
    pre = round(sum(list(dict.values(ndi))),2)
    return pre