def lingua_p(palavra):
    '''Dada uma palavra em português, retorna a mesma palavra na lingua do P
    str->str'''
    novapalavra=''
    
    for i in range(len(palavra)):
        if palavra[i] in 'AEIOUaeiou':
            novapalavra=novapalavra+palavra[i]
        if palavra[i] not in 'AEIOUaeiou' and i==0:
            novapalavra=novapalavra+palavra[i]
        if palavra[i] not in 'AEIOUaeiou' and palavra[i-1] not in 'AEIOUaeiou' and i!=0:
            novapalavra=novapalavra+palavra[i]
        if palavra[i] not in 'AEIOUaeiou' and palavra[i-1] in 'AEIOUaeiou' and i!=0:
            novapalavra=novapalavra+'p'+palavra[i-1]+palavra[i]
    return str.lower(novapalavra)