def inverte(frase):
    '''dado uma frase, essa funcao retorna a mesma frase porem na orem inversa, 
    sem letras maiusculas e sem a pontuacao'''
    frase1 = str.replace(frase, '.', ' ')
    frase2 = str.replace(frase1, '!', ' ')
    frase3 = str.replace(frase2, '?', ' ')
    frase4 = str.replace(frase3, '...', ' ')
    frase5 = str.replace(frase4, '-', ' ')
    frase6 = str.replace(frase5, ',', ' ')
    frase7 = str.replace(frase6, ':', ' ')
    frase8 = str.replace(frase7, ';', ' ')
    frase9 = str.lower(frase8)
    frase10 = str.split(frase9)
    frase11 = frase10[::-1]
    frase12 = str(frase11)
    frase13 = str.replace(frase12,'[','')
    frase14 = str.replace(frase13,']','')
    frase15 = str.replace(frase14,',',' ')
    return frase12