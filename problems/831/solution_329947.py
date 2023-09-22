def lingua_p(string):
    '''
    adiciona p apos uma vogal e repete a vogal
    '''
    vogais="aeiou"
    palavra=""
    for identificador in string:
        if identificador in vogais:
            palavra = palavra + "p"+identificador+"p"
            palavra = palavra.lower()
        else:
            palavra = palavra + identificador
            palavra = palavra.lower()
            
    return palavra