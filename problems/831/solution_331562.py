def lingua_p (palavra):
    '''retorna a palavra traduzida na lingua do p
    str->str'''
    palavraP = ''
    for i in palavra:
        if i in 'aeiouAEIOU':
            palavraP = palavraP + i + 'p'
        else:
            palavraP = palavraP + i
    return palavraP