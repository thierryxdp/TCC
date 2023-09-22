def lingua_p(palavra):
    '''retorne a palavra traduzida para a lingua do p'''
    minuscula = palavra.lower()
    nova_palavra = ''
    vogais = 'aeiouãáéíóú'
    for p in minuscula:
        nova_palavra += p 
        if p in vogais:
            nova_palavra =+ 'p' + p 
    return nova_palavra