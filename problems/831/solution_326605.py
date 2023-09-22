def lingua_p(str):
    novaPalavra = ""
    for caracter in str:
        if caracter in "aeiouAEIOU":
            novaPalavra = novaPalavra + caracter + "p" + caracter
        else:
            novaPalavra = novaPalavra
    return novaPalavra