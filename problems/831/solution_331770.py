def lingua_p (palavra):
     minu = palavra.lower()
    novaPalavra = ''
    vogais = 'aeiouãáéíóú'
    for p in minusculo:
        novaPalavra += p
        if p in vogais:
            novaPalavra += 'p' + p

    return novaPalavra