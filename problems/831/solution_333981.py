def lingua_p(palavra):
    #traduz para a língua do P.
    vogais = ['a','e','i','o','u','A','E','I','O','U','á','é','í','ó','ú','â','ê','î','ô','û']
    resultado = ''
    for l in palavra:
        if l in vogais:
            resultado += l + 'p' + l
        else:
            resultado += l
    return resultado