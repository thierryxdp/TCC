def uppCons(frase):
    '''função que recebe uma frase e retorna as consoantes em maiuscula
    str->str'''
    frase_tratada=''
    for caractere in frase:
        if caractere in 'blabla':
            caractere= str.upper(caractere)
            frase_tratada= frase_tratada + caractere
    return frase_tratada