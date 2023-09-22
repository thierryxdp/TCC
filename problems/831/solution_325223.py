def lingua_p(palavra):
    '''traduz a palavra para a lingua do p
    string -> string'''
    palavra = str.lower(palavra)
    fraseNova = ""
    for i in palavra:
        if i in 'aeiou':
            fraseNova = fraseNova + i + "p"
        else:
            fraseNova = fraseNova + i
    i = i + 1
    return fraseNova