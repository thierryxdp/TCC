def lingua_p(palavra):
    min=palavra.lower()
    novapalavra=''
    vogais='aeiouãáéíóú'
    for p in min:
        novapalavra+=p
        if p in vogais:
            novapalavra=+'p'+´p
    return novapalavra