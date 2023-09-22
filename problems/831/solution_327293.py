def lingua_p(palavra):
    '''função que receba uma palavra e retorne a palavra traduzida para a 
    língua do p, ou seja, após cada vogal da palavra original, é inserida a
    sequência de letras 'p' mais a vogal original
    str -> str'''
    palavra = str.lower(palavra)
    palavra_traduzida = ''
    for letra in palavra:
        if letra in 'aeiou':
            silaba = 'p'+letra
        palavra_traduzida  += silaba
    return palavra_traduzida