def lingua_p(palavra):
    '''
	função que recebe uma palavra e retorna esta mesma palavra traduzida para a lingua do P, em que após a cada vogal da palavra orginal, é inserida a sequência de letras 'p'mais a vogal original;
    str -> str
    '''
    vogais = 'aeiou'
    traducao = ''
    palavra = str.lower(palavra)
    for letra in palavra:
        if letra in vogais:
            traducao = traducao + letra + 'p'+ letra
        else:
            traducao = traducao + letra
    return traducao