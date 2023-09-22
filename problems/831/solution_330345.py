def lingua_p(palavra):
    '''Retorna a palavra de entrada na língua do p.
    str->str'''
    palavra_minuscula=str.lower(palavra)
    palavra_p=''
    for letra in palavra_minuscula:
        if letra in 'aeiou':
            letra=letra+'p'+letra
        palavra_p=palavra_p+letra
    return palavra_p