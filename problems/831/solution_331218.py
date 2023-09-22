def lingua_p(palavra):
    vogais = ['a', 'e', 'i', 'o', 'u',
             'á', 'é', 'í', 'ó', 'ú']
    palavra_p = ''
    for letra in palavra:
        if letra not in vogais:
            palavra_p += letra
        else:
            palavra_p += letra + 'p' + letra
    return palavra_p