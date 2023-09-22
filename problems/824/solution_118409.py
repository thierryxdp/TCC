def uppCons(f):
    'define yma funçao que seleciona os caracteres de uma frase que sao consoantes e os coloca em letra maiuscula str->str'
    newf = ''
    for lcons in f:
        if lcons in 'ZXCVBNMSDFGHJKLQWRTYPzxcvbnmsdfghjklqwçrtyp':
            newf += lcons.upper()
        else:
            newf += lcons
    return newf