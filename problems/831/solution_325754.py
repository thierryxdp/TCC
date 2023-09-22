def lingua_p(palavra):
    for letra in palavra:
        if letra in ['a','e','i','o','u']:
            ppalavra=str.replace (palavra,letra,(letra+'p'))
    return ppalavra