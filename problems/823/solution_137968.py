def faltante(l):
    """Função que dada uma lista de 1 a n com um dos números faltando, retorna qual número está faltando"""
    """list--->int"""
    i=1
    while l[i-1]==i:
        i+=1
        if i not in l:
            resposta=i
    return resposta