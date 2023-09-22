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
    frase.reverse()
    frase = str.join(" ",frase)
    return frase