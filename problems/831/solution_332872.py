def lingua_p(palavra):
    palavra = palavra.lower()
    palavra_p = ''
    for letra in palavra:
        if letra in 'bcdfghjklmnpqrstvwxyzç':
            palavra_p += letra
        else:
            palavra_p += letra + 'p'
    return palavra_p