def lingua_p(palavra):
    '''Função que, dada uma palavra, muda ela para a lingua do p.
    str --> str'''
    p = ''
    for letra in palavra:
        p = p + letra
        if letra in 'AEIOUaeiouáéíóúãõêâîôÁÉÍÓÚÃÕÊÂÎÔ':
            p = p + 'p' + letra
    return str.lower(p)