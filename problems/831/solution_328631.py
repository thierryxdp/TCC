def lingua_p(plvra):
    '''dada uma palavra retorna ela traduzida para a lingua do p
    str -> str'''
    
    vogal = 'aeiou'
    strRtr = ''
    for letra in plvra:
        if(letra.lower() in vogal):
            strRtr += 'p' + letra
        else:
            strRtr += letra
    return strRtr