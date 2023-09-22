def lingua_p(palavra):
    minu=palavra.lower()
    novapalavra=''
    vogais='aeiouãáéíóú'
    for p in minu:
        novapalavra+=p
        if p in vogais:
            novapalavra=+'p'+´p
    return novapalavra