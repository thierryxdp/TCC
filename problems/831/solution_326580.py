def lingua_p(palavra):
    '''Dada uma palavra, retorna a mesma na lingua do P.
    str -> str'''
    palavra = palavra.lower()
    strFinal = ''
    i = 0
    f = 0

    for caractere in palavra:
        if caractere in 'aeiouãáéú':
            strFinal += palavra[i:f] + caractere + 'p' + caractere
            i = f + 1
        f += 1
    strFinal += palavra[i:]
    return strFinal