def lingua_p(palavra):
    ''' dada uma palavra qualquer em português, retorna a mesma palavra
    traduzida para a língua do P.
    str --> str '''
    palavra_traduzida = ''
    for letra in palavra:
        if letra in 'aeiouáéíóú':
            palavra_traduzida += letra + 'p' + letra
        else:
            palavra_traduzida += letra
            
            
    
    return palavra_traduzida