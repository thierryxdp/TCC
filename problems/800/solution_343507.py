def total(lis, dic):
    """Função que recebe uma lista e um dicionário e
retorna a soma das chaves da lista que estão no dicio.
"""
    ndi = {}
    for c in range (0, len(dic)-1, 1):
    	if lis[c] in dic:
        	ndi[lis[c]] = dict.get(dic, lis[c])
    return lis[0]