def inverte (frase: str)-> str:
    '''retorna uma frase que contenha as palavras da frase dada na ordem
    inversa, sem letras maúsculas e sem pontuação'''
    frase= str.replace (frase, '-', ' ')
    frase= str.replace (frase, ',', ' ')
    frase= str.replace (frase, ':', ' ')
    frase= str.replace (frase, ';', ' ')
    frase= str.replace (frase, '...', ' ')
    frase= str.replace (frase, '.', ' ')
    frase= str.replace (frase, '?', ' ')
    frase= str.replace (frase, '!', ' ')
    frase = str.lower(frase)
    frase = str.split(frase)
    
    return str(frase[-1]) + ' ' + str(frase[-2]) + ' ' + str(frase[-3]) + ' ' + str(frase[-4]) + ' ' + str(frase[-5])' ' + str(frase[-6]) + ' ' + str(frase[-7])' ' + str(frase[-8]) + ' ' + str(frase[-9])