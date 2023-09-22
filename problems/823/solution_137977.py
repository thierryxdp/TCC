def faltante(l):
    """Função que dada uma lista de 1 até n, que tem um número faltante, retorna qual número não esta na lista"""
    """list--->int"""
    i=0
    while i<len(l):
        if i+1!=l[i]:
            return l[i]
        i+=1