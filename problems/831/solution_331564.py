def lingua_p (palavra):
    '''retorna a palavra traduzida na lingua do p
    str->str'''
    palavraP = ''
    palavraMin = str.lower(palavra)
    for i in palavraMin:
        if i in 'aeiouáàéíúó':
            palavraP = palavraP + i + 'p' + i
        else:
            palavraP = palavraP + i
    return palavraP