def lingua_p(palavra):
    ppalavra = ''
    for letra in palavra:
        if letra in 'AEIOUÁÉÍÓÚÃÂÔÊaeiouáéíóúâêîôûã':
            ppalavra = ppalavra +palavra[str.index(palavra,letra): str.index(palavra, letra)+1] + 'p' + letra
        else:
            ppalavra = ppalavra + letra
    return ppalavra