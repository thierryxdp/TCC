v = 'aeiou'
def lingua_p(palavra):
    ''' traduz a palavra para a lingua do p'''
    palavra = list(palavra.lower())
    for i in palavra:
        if i in v:
            i = i + 'p' + i
    palavra = ''.join(palavra)
    return palavra