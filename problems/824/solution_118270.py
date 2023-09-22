def uppCons(frase):
    '''
    Funçao que recebe uma frase e retorna a mesma
    com as consoantes em maiusculas
    str -> str
    '''
    letra = 1
    while letra < len(frase):
        if frase[letra] in 'qwrtypçlkjhgfdszxcvbnm':
        	C = str.upper(frase[letra])
            frase= str.replace(frase,frase[letra], C, letra)
		letra=letra+1
    return frase