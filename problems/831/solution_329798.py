def lingua_p(palavra):
    ppalavra = ''
    for letra in palavra:
        if letra in 'AEIOUÁÉÍÓÚÃÂÔÊaeiouáéíóúâêîôûã':
            ppalavra = ppalavra + letra + 'p' + letra
        else:
            ppalavra = ppalavra + letra
    return ppalavra