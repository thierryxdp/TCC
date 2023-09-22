def lingua_p(palavra):
    '''Retorna a palavra com a letra p entre as vogais; str->str'''
    traduzido=''
    for letra in palavra:
        if letra in 'aeiouáéíóú':
            traduzido+=letra+'p'+letra
        else:
            traduzido+=letra
    return traduzido