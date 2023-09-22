def lingua_p(palavra):
    '''Dada uma palavra em português, retorna a mesma palavra na lingua do P
    str->str'''
    novapalavra=''
    
    for i in range(len(palavra)):
        if palavra[i] in 'AEIOUaeiouáâãéêíîôõóúû':
            novapalavra=novapalavra+palavra[i]+'p'+palavra[i]
        if palavra[i] not in 'AEIOUaeiouáâãéêíîôõóúû':
            novapalavra=novapalavra+palavra[i]
        
    return str.lower(novapalavra)