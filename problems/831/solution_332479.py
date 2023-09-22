def lingua_p (palavra):
    '''
    Fução que recebe uma palavra e a "traduz" para a
    linguagem do P.
    Uma palavra é traduzida para a lingugem do P quando,
    apos cada vogal da palavra original, é inserida a sequencia
    de letras 'p' mais a vogal original
    string--->string
    '''
    palavra=str.lower(palavra)
    for n in palavra:
        if n in 'aeiou':
            n=n+'p'+n
    return palavra