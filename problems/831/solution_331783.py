def lingua_p(x):
    """Função que recebe uma palavra e a traduz para lingua do p"""
    """str-->str"""
    i=0
    str.lower(x)
    resposta=''
    while i<len(x):
        if x[i] in 'aeiou':
            resposta+=x[i]+'p'+x[i]
        else:
            resposta+=x[i]
        i+=1
        return resposta