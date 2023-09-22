def lingua_p(palavra):
    ''' docs
    str --> str'''
    
    for letra in palavra:
        if letra in 'aeiouáéíóú':
            # adicionar o P
            palavra_traduzida += p + letra
        else:
            palavra_traduzida += letra
            
    return palavra_traduzida