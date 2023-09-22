def uppCons(frase_original):
    '''funçao que calcula e retorna uma frase com todas
    suas consoantes em maiusculas e os outros caracteres
    iguais a frase original. str->str'''
    i = 0
    consoantes = ""
    while i<len(frase_original):
        if frase_original[i] in "bcdfghjklmnpqrstvwxyzçBCDFGHJKLMNPQRSTVWXYZÇ":
            consoantes = str.replace(frase_original, frase_original[i], str.upper(frase_original[i]))
            frase_original = consoantes
        i += 1
    return frase_original