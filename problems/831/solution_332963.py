def lingua_p(palavra):
    '''função em que dada uma palavra (em portugues) e retorne esta mesma palavra
    traduzida para a lingua do P; str -> str'''
    vogais= ''
    m= palavra.lower()
    v= 'AEIOUaeiou'
    for letras in m:
        vogais= vogais + letras
        if letras in v:
            vogais += + 'p'  + p
    return vogais