def lingua_p(palavra):
    '''Dada uma palavra, reorne a mesma na língua do p; str->str'''
    palavra=str.lower(palavra)
    P=str()
    for l in palavra:
        if l in 'aeiouáéíóúâêôûãõ':
            P=P+l+'p'+letra
        else:
            P=P+l
    return P