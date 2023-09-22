def lingua_p(palavra):
    ''' dada uma palavra qualquer em português, retorna a mesma palavra
    traduzida para a língua do P.
    str --> str '''
    for letra in palavra:
        if letra in 'aeiou':
            palavra_traduzida += p + letra
        else:
            palavra_traduzida += letra
            
            
    
    return palavra_traduzida