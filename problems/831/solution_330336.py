def lingua_p(palavra):
    '''Função que dada uma palavra, retorna a mesma traduzida na lingua
    do ''P'' '''
    x = ''
    for letra in palavra:
        if letra in 'AÁEÉIÍOÓUÚaáeéiíoóuú':
            x += letra+'p'+letra
        else:
            x += letra
    return str.lower(x)