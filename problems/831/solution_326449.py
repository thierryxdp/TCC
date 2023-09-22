def lingua_p(palavra):
    '''funçao que dada uma palavra traduz pra lingua p'''
    palavraNova = ''
    for c in range(0,len(palavra)):
        if palavra[c] in 'aeiouAEIOU':
            palavraNova += 'p'
           	palavraNova += palavra
        else:
          	palavraNova += palavra
    return palavraNova