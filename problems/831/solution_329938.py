def lingua_p(palavra):
    '''Retorna a palavra inserida traduzida para a língua do P
str -> str'''
    i=0
    palavranova=''
    while i<len(palavra):
        if palavra[i] in 'aeiouáéíóúâêôãõAEIOUÁÉÍÓÚÂÊÔÃÕ':
            palavranova=palavranova+palavra[i]+'p'+palavra[i]
        else:
            palavranova=palavranova+palavra[i]
        i=i+1
    return palavranova