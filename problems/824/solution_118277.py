def uppCons(frase):
    '''
    Funçao que recebe uma frase e retorna a mesma
    com as consoantes em maiusculas
    str -> str
    '''
    letra = 1
    while letra < len(frase):
        if frase[letra] in 'cqwrtyplkjhgfdszxvçbnmQWRTYPÇLKJHGFDSZXCVBNM':
        	letra2 = str.upper(frase[letra])
            frase= str.replace(frase,frase[letra], letra2, letra)
		letra=letra+1
    return frase