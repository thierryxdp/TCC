def lingua_p(palavra):
    palavra_minuscula = str.lower(palavra)
    palavra_traduzida = ''
    for letra in palavra:
        if letra in 'aeiouáéíóú':
            palavra_traduzida = palavra_traduzida + letra +'p' + letra
        else:
            palavra_traduzida = palavra_traduzida + letra
    return palavra_traduzida