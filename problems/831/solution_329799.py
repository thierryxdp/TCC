def lingua_p(palavra):
    ''' dada uma palavra p, ira traduzi-la pra a lingua p. str = str'''
    ppalavra = ''
    for letra in palavra:
        if letra in 'AEIOUÁÉÍÓÚÃÂÔÊaeiouáéíóúâêîôûã':
            ppalavra = ppalavra + letra + 'p' + letra
        else:
            ppalavra = ppalavra + letra
    return ppalavra