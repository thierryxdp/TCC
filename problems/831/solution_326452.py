def lingua_p(palavra):
    '''funçao que dada uma palavra traduz pra lingua p'''
    palavraNova = ''
    for c in range(0,len(palavra)):
        if palavra[c] in 'aeiouAEIOU':
            palavraNova += palavra[c]
            palavraNova += 'p'
            palavraNova += palavra[c]
        else:
            palavraNova += palavra[c]
    return palavraNova