def lingua_p(palavra):
    palavra_traduzida = ''
    for letra in palavra:
        if letra in 'aeiouáàâãéêíóõú':
            palavra_traduzida += letra + 'p' + letra
        else:
            palavra_traduzida += letra
    
    return palavra_traduzida