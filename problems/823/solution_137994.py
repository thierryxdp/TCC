def faltante(l):
    """Função que dada uma lista de 1 até n, que tem um número faltante, retorna qual número não esta na lista"""
    """list--->int"""
    i=0
    while i<len(l):
        if i+1!=l[i]:
            return i+1
        elif i==len(l)-1 and i+1==l[i]:
            return i+2
        elif l[0]!=1:
            return 1
        i+=1