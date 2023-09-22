def lingua_p(palavra):
    '''traduz a palavra para a lingua do p
    string -> string'''
    palavra = str.lower(palavra)
    novaPalavra = ""
    for i in palavra:
        if i in 'aeiou':
            novaPalavra = novaPalavra + i + "p"
        else:
            novaPalavra = novaPalavra + i
    i = i + 1
        return novaPalavra