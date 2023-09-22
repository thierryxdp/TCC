def lingua_p(string):
    '''
    adiciona p apos uma vogal e repete a vogal
    '''
    vogais="aeiouáéíú"
    palavra=""
    for identificador in string:
        if identificador in vogais:
            palavra = palavra + identificador+"p"+identificador
            palavra = palavra.lower()
        else:
            palavra = palavra + identificador
            palavra = palavra.lower()
            
    return palavra