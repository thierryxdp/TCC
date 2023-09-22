def lingua_p(palavra):
    '''Esta função traduz uma palavra em portugues para a lingua p.
str->str'''
    palavra_traduzida=''
    for letra in palavra:
        if letra in 'aeiouáéíóú:
            palavra_traduzida+=letra+'p'+letra
        else:
            palavra_traduzida+=letra
    return palavra_traduzida