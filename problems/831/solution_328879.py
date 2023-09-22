def lingua_p(palavra):
    '''Traduz uma palavra em português para a língua do p;
       str -> str'''
    palavra_traduzida = ''
    for letra in palavra:
        if str.lower(letra) in 'aeiouáéíóúãõâêîôûà':
            palavra_traduzida = palavra_traduzida + letra + 'p' + letra
        else:
            palavra_traduzida = palavra_traduzida + letra
    return str.lower(palavra_traduzida)