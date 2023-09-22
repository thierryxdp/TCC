def lingua_p (palavra):
    '''
    Fução que recebe uma palavra e a "traduz" para a
    linguagem do P.
    Uma palavra é traduzida para a lingugem do P quando,
    apos cada vogal da palavra original, é inserida a sequencia
    de letras 'p' mais a vogal original
    string--->string
    '''
    contador=0
    contador2=2
    palavra=str.lower(palavra)
    for n in palavra:
        if n in 'aeiou':
            palavra=str(palavra[0:contador]+n+'p'+n+contador2:]
        contador=contador+1                        
    return palavra