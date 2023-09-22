def inverte(texto):
    ''' '''
    frase = str.replace(texto, "-", " ")
    frase1 = str.replace(frase, ",", " ")
    frase2 = str.replace(frase1, "...", " ")
    frase3 = str.replace(frase2, "..", " ")
    frase4 = str.replace(frase3, ".", " ")
    frase5 = str.replace(frase4, ";", " ")
    frase6 = str.replace(frase5, "!", " ")
    frase7 = str.replace(frase6, "?", " ")
    frase_minuscula = str.lower(frase7)
    frase_nova = frase_minuscula[::-1]