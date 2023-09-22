def lingua_p(palavra):
    '''funcao que transforma uma palvra normal em uma palavra na lingua do p
    str->str'''
    p_palavra= ''
    for i in palavra:
        if 'AEIOUaeiou' in palavra:
            p_palavra= i+'p'
    return p_palavra