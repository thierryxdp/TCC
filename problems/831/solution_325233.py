def lingua_p(palavra):
    '''traduz a palavra para a lingua do p
    string -> string'''
    palavra = str.lower(palavra)
    fraseNova = ""
    indice = 0
    for i in palavra:
        if i in 'aeiou':
            fraseNova = fraseNova + i + "p" + i
        else:
            fraseNova = fraseNova + i
    indice = indice + 1
    return fraseNova