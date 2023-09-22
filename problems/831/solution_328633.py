def lingua_p(plvra):
    '''dada uma palavra retorna ela traduzida para a lingua do p
    str -> str'''
    
    vogal = 'aeiouéáúóíêâûôî'
    strRtr = ''
    for letra in plvra:
        if(letra.lower() in vogal):
            strRtr += letra + 'p' + letra
        else:
            strRtr += letra
    return strRtr