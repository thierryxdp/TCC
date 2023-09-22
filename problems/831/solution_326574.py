def lingua_p(palavra):
    palavra = str.lower(palavra)
    novapalavra = ''
    for i in palavra:
        if i in 'abcde':
            novapalavra += i + 'p' + i
        else:
            novapalavra += i
    return novapalavra