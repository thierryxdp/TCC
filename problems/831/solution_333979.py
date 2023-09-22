def lingua_p(palavra):
    #traduz para a língua do P.
    vogais = ['a','e','i','o','u','A','E','I','O','U']
    resultado = ''
    for l in palavra:
        if l in vogais:
            resultado += l + 'p'
        else:
            resultado += l
    return resultado