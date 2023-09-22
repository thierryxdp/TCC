def lingua_p(palavra):
    ''' docs
    str --> str'''
    palavra_traduzida = ''
    
    for letra in palavra:
        if letra in 'aeiou':
            # adicionar o P
            palavra_traduzida += letra + 'p' + letra
        else:
            palavra_traduzida += letra
    
    return palavra_traduzida