def lingua_p(palavra):
    """Retorna a palavra traduzida para língua do p;
       str -> str
       Parametro:
       palavra: palavra qualquer
    """
    novapalavra = ''
    for i in range(len(palavra)):
        minu=str.lower(palavra[i])
        if minu in 'aeiouã':
            novapalavra += palavra[i] + 'p' + palavra[i]
        else:
            novapalavra += palavra[i]
    return str.lower(novapalavra)