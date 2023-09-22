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
    while contador<len(palavra):
        if palavra[contador] in 'aeiou':
            palavra[contador]=palavra[contador]+'p'+palavra[contador]
            
        contador=contador+1                        
    return palavra