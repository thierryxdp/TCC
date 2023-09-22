def uppCons(frase):
    '''função que recebe uma frase e retorna as consoantes em maiuscula
    str->str'''
    frase_tratada=' '
    i = 0
    while i < len(frase):
        caractere = frase[i]
        if caractere in 'blabla':
            caractere= str.upper(caractere)
            frase_tratada = frase_tratada + caractere
            i=i+1
     return frase_tratada