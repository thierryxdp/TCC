def inverte (frase):
    '''
    	essa função recebe uma frase e retorna uma outra frase que é a primeira original mas
        na ordem inversa, com as letras minúsculas e sem pontuação 
        str->str
    '''
    frase = str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'-', ' '),',', ' '),':', ' '),';', ' '),'.', ' '),'!', ' '),'?', ' ')
    x = str.split(str.lower(frase))
    y = x[::-1]
    z = str.join(' ',y)
    return z