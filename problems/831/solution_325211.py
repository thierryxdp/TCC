def lingua_p(palavra):
    '''traduz a palavra para a lingua do p
    string -> string'''
    palavra = str.lower(palavra)
    for i in palavra:
        if i in 'aeiou':
            palavra = palavra[:i] + "p" + palavra[i:]
    return palavra